EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026",
    "Celebrities who don't like cheese",
]

HEADER_HTML = """
<div class="dr-brand">
    <div class="dr-mark">
        <span class="dr-bar dr-bar-1"></span>
        <span class="dr-bar dr-bar-2"></span>
        <span class="dr-bar dr-bar-3"></span>
    </div>
    <div class="dr-titles">
        <h1>Deep<span class="dr-sep">/</span>Research</h1>
        <p>Multi-search web investigation</p>
    </div>
</div>
"""

CSS = """
/* Palette: always dark, same look in Gradio's light and dark modes */
:root, .dark, .gradio-container {
    --dr-bg: #0B0F19;       /* Obsidian Void: page background */
    --dr-surface: #1E293B;  /* Surface Tint: inputs and containers */
    --dr-text: #F8FAFC;     /* Crisp Cream: all text */
    --dr-accent: #38BDF8;   /* Intelligence Blue: actions, highlights, loading */
    --dr-muted: #94A3B8;    /* secondary text */
    --dr-line: #334155;     /* borders and dividers */

    /* Gradio theme variables, so built-in parts (loaders, labels, inputs) match */
    --body-background-fill: var(--dr-bg);
    --background-fill-primary: var(--dr-bg);
    --background-fill-secondary: var(--dr-surface);
    --block-background-fill: var(--dr-surface);
    --input-background-fill: var(--dr-bg);
    --body-text-color: var(--dr-text);
    --body-text-color-subdued: var(--dr-muted);
    --block-label-text-color: var(--dr-text);
    --block-title-text-color: var(--dr-text);
    --border-color-primary: var(--dr-line);
    --color-accent: var(--dr-accent);
    --color-accent-soft: rgba(56, 189, 248, 0.16);
    --loader-color: var(--dr-accent);
    --link-text-color: var(--dr-accent);
    color-scheme: dark;
}

html, body, gradio-app {
    background: var(--dr-bg) !important;
}

.gradio-container {
    max-width: 1080px !important;
    margin: 0 auto !important;
    padding: 2.5rem 2rem 4rem !important;
    background: var(--dr-bg) !important;
    color: var(--dr-text) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif !important;
}

/* === HEADER === */
.dr-brand {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 1.4rem;
    padding-bottom: 1.25rem;
    border-bottom: 2px solid var(--dr-line);
    margin-bottom: 2.5rem;
}

.dr-mark {
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 38px;
}

.dr-bar { height: 7px; display: block; }
.dr-bar-1 { background: var(--dr-accent); width: 100%; }
.dr-bar-2 { background: var(--dr-text); opacity: 0.55; width: 70%; }
.dr-bar-3 { background: var(--dr-text); opacity: 0.25; width: 45%; }

.dr-titles h1 {
    font-size: clamp(1.8rem, 4vw, 2.6rem);
    font-weight: 900;
    letter-spacing: -0.045em;
    margin: 0;
    line-height: 0.95;
    text-transform: uppercase;
    color: var(--dr-text);
}

.dr-sep {
    color: var(--dr-accent);
    font-weight: 300;
    margin: 0 0.04em;
}

.dr-titles p {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
    font-size: 0.7rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    margin: 0.55rem 0 0;
    color: var(--dr-muted);
}

/* === QUERY ROW === */
.dr-query-row {
    gap: 0 !important;
    align-items: stretch !important;
}

#dr-query, #dr-query > div, #dr-query .wrap, #dr-query .form, #dr-query .block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

#dr-query textarea, #dr-query input {
    background-color: var(--dr-surface) !important;
    /* blue search icon inside the bar */
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%2338BDF8' stroke-width='2.4' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='m20 20-3.5-3.5'/%3E%3C/svg%3E") !important;
    background-repeat: no-repeat !important;
    background-position: 1.1rem 50% !important;
    color: var(--dr-text) !important;
    border: 2px solid var(--dr-line) !important;
    border-right: none !important;
    border-radius: 0 !important;
    padding: 1.05rem 1.2rem 1.05rem 3rem !important;
    font-size: 1.05rem !important;
    font-family: inherit !important;
    box-shadow: none !important;
    line-height: 1.45 !important;
    resize: none !important;
    min-height: 56px !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
}

#dr-query textarea:focus, #dr-query input:focus {
    outline: none !important;
    border-color: var(--dr-accent) !important;
    box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.25) !important;
}

#dr-query textarea::placeholder, #dr-query input::placeholder {
    color: var(--dr-muted) !important;
    opacity: 1 !important;
}

/* Primary buttons: Investigate and Start research */
#dr-run, #dr-clarify button {
    background: var(--dr-accent) !important;
    color: var(--dr-bg) !important;
    border: 2px solid var(--dr-accent) !important;
    border-radius: 0 !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.14em !important;
    font-size: 0.85rem !important;
    box-shadow: none !important;
    transition: background 0.15s, color 0.15s, transform 0.08s !important;
    min-width: 150px !important;
    padding: 1rem 1.5rem !important;
}

#dr-run:hover, #dr-clarify button:hover {
    background: transparent !important;
    color: var(--dr-accent) !important;
}

#dr-run:active, #dr-clarify button:active { transform: translate(1px, 1px) !important; }

#dr-run:focus-visible, #dr-clarify button:focus-visible {
    outline: 2px solid var(--dr-text) !important;
    outline-offset: 2px !important;
}

/* === EXAMPLES === */
.dr-examples-label {
    font-family: ui-monospace, SFMono-Regular, monospace;
    font-size: 0.65rem;
    letter-spacing: 0.28em;
    color: var(--dr-muted);
    text-transform: uppercase;
    margin: 2rem 0 0.85rem 0;
    display: flex;
    align-items: center;
    gap: 0.85rem;
}

.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--dr-line);
}

#dr-examples, #dr-examples > div, #dr-examples .wrap, #dr-examples .block {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}

#dr-examples label, #dr-examples .label-wrap, #dr-examples > div > .label-wrap {
    display: none !important;
}

#dr-examples table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: auto !important;
    background: transparent !important;
    border: none !important;
}

#dr-examples thead { display: none !important; }

#dr-examples tbody { background: transparent !important; }

#dr-examples tr {
    background: transparent !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    border: none !important;
}

#dr-examples td, #dr-examples button {
    background: var(--dr-surface) !important;
    border: 1.5px solid var(--dr-line) !important;
    padding: 0.7rem 1.05rem !important;
    cursor: pointer !important;
    transition: border-color 0.15s, color 0.15s, transform 0.1s !important;
    font-size: 0.9rem !important;
    color: var(--dr-text) !important;
    border-radius: 0 !important;
    margin: 0 !important;
    text-align: left !important;
    box-shadow: none !important;
}

#dr-examples td:hover, #dr-examples button:hover {
    border-color: var(--dr-accent) !important;
    color: var(--dr-accent) !important;
    transform: translateY(-1px);
}

/* === CLARIFICATION PANEL === */
#dr-clarify {
    margin-top: 2.5rem !important;
    background: var(--dr-surface) !important;
    border: 1.5px solid var(--dr-line) !important;
    border-radius: 0 !important;
    padding: 1.5rem !important;
    gap: 1.1rem !important;
}

#dr-clarify .block, #dr-clarify .form, #dr-clarify .wrap {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

#dr-clarify label span, #dr-clarify [data-testid="block-info"] {
    background: transparent !important;
    color: var(--dr-text) !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    line-height: 1.4 !important;
    border: none !important;
    padding: 0 !important;
    margin-bottom: 0.45rem !important;
}

#dr-clarify textarea {
    background: var(--dr-bg) !important;
    color: var(--dr-text) !important;
    border: 1.5px solid var(--dr-line) !important;
    border-radius: 0 !important;
    padding: 0.75rem 0.9rem !important;
    font-size: 0.95rem !important;
    box-shadow: none !important;
}

#dr-clarify textarea::placeholder { color: var(--dr-muted) !important; }

#dr-clarify textarea:focus {
    outline: none !important;
    border-color: var(--dr-accent) !important;
    box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2) !important;
}

#dr-clarify button { align-self: flex-start !important; }

/* === REPORT === */
#dr-report {
    margin-top: 2.5rem !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--dr-text) !important;
    min-height: 40px;
}

#dr-report > div, #dr-report .prose {
    background: transparent !important;
    color: var(--dr-text) !important;
}

#dr-report:not(:empty) {
    border-top: 1px solid var(--dr-line) !important;
    padding-top: 1.75rem !important;
}

#dr-report h1 {
    font-size: 1.85rem;
    font-weight: 900;
    color: var(--dr-text);
    border-bottom: 2px solid var(--dr-accent);
    padding-bottom: 0.45rem;
    margin: 1.5rem 0 1rem;
    letter-spacing: -0.025em;
}

#dr-report h2 {
    font-size: 1.35rem;
    color: var(--dr-accent);
    font-weight: 800;
    margin-top: 1.75rem;
    letter-spacing: -0.015em;
}

#dr-report h3 {
    font-size: 1.1rem;
    color: var(--dr-text);
    font-weight: 800;
    margin-top: 1.5rem;
}

#dr-report p { line-height: 1.7; }

#dr-report a {
    color: var(--dr-accent);
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 3px;
}

#dr-report a:hover { color: var(--dr-text); }

#dr-report strong { color: var(--dr-text); }

#dr-report mark {
    background: rgba(56, 189, 248, 0.16);
    color: var(--dr-accent);
    padding: 0 0.2em;
}

#dr-report code {
    background: var(--dr-surface);
    color: var(--dr-text);
    border: 1px solid var(--dr-line);
    padding: 0.1rem 0.4rem;
    font-size: 0.92em;
    border-radius: 0;
}

#dr-report pre {
    background: var(--dr-surface);
    border: 1.5px solid var(--dr-line);
    border-radius: 0;
    padding: 1rem 1.25rem;
}

#dr-report blockquote {
    border-left: none !important;
    background: var(--dr-surface);
    padding: 1rem 1.25rem;
    margin: 1rem 0;
    color: var(--dr-text);
}

#dr-report ul, #dr-report ol { padding-left: 1.5rem; }
#dr-report li { margin: 0.3rem 0; line-height: 1.6; }

#dr-report table {
    border-collapse: collapse;
    border: 1.5px solid var(--dr-line);
}

#dr-report th, #dr-report td {
    border: 1px solid var(--dr-line);
    padding: 0.5rem 0.85rem;
    text-align: left;
}

#dr-report th {
    background: var(--dr-surface);
    font-weight: 800;
    color: var(--dr-accent);
}

footer { display: none !important; }

@media (max-width: 700px) {
    .gradio-container { padding: 1.5rem 1rem 3rem !important; }
    .dr-query-row { flex-direction: column !important; }
    #dr-query textarea, #dr-query input { border-right: 2px solid var(--dr-line) !important; }
    #dr-run { width: 100% !important; }
}
"""

JS = """
() => {
    const focus = () => {
        const el = document.querySelector("#dr-query textarea, #dr-query input");
        if (el) { el.focus(); return true; }
        return false;
    };
    if (!focus()) {
        let tries = 0;
        const i = setInterval(() => {
            if (focus() || ++tries > 20) clearInterval(i);
        }, 100);
    }
}
"""
