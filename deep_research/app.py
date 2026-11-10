import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
from clarification_agent import CLARIFICATION_QUESTIONS
from styles import CSS, JS, EXAMPLES, HEADER_HTML

load_dotenv(override=True)


async def clarify(query: str):
    """Step 1: get clarifying questions and show one answer box per question."""
    if not query or not query.strip():
        return [[], gr.update(visible=False), "Please type a research question first."] + [
            gr.update(visible=False) for _ in range(CLARIFICATION_QUESTIONS)
        ]

    questions = (await ResearchManager().clarify(query))[:CLARIFICATION_QUESTIONS]
    boxes = [
        gr.update(label=questions[i], value="", visible=True) if i < len(questions)
        else gr.update(value="", visible=False)
        for i in range(CLARIFICATION_QUESTIONS)
    ]
    message = "Answer any of these to sharpen the research (blank answers are skipped), then press **Start research**."
    return [questions, gr.update(visible=True), message] + boxes


async def run(query: str, questions: list[str], *answers: str):
    """Step 2: run the research with the query plus the user's answers."""
    clarifications = list(zip(questions or [], answers))
    async for status_update in ResearchManager().run(query, clarifications):
        yield status_update


with gr.Blocks(title="Deep Research") as ui:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes="dr-query-row"):
        query_textbox = gr.Textbox(
            placeholder="Type a research question...",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Investigate", variant="primary", elem_id="dr-run", scale=1)

    gr.HTML('<div class="dr-examples-label">Try one</div>')
    gr.Examples(examples=EXAMPLES, inputs=query_textbox, elem_id="dr-examples")

    questions_state = gr.State([])
    with gr.Column(visible=False, elem_id="dr-clarify") as clarify_column:
        answer_boxes = [gr.Textbox(visible=False, lines=2) for _ in range(CLARIFICATION_QUESTIONS)]
        start_button = gr.Button("Start research", variant="primary")

    report = gr.Markdown(elem_id="dr-report")

    clarify_outputs = [questions_state, clarify_column, report] + answer_boxes
    run_button.click(clarify, inputs=query_textbox, outputs=clarify_outputs)
    query_textbox.submit(clarify, inputs=query_textbox, outputs=clarify_outputs)

    start_button.click(
        lambda: gr.update(visible=False), outputs=clarify_column
    ).then(run, inputs=[query_textbox, questions_state] + answer_boxes, outputs=report)


if __name__ == "__main__":
    ui.launch(css=CSS, js=JS, theme=gr.themes.Base())
