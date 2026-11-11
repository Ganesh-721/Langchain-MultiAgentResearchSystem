import streamlit as st

from src.pipelines.pipelines import run_research_pipeline


st.set_page_config(
    page_title="Research Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #080b16;
        --panel: rgba(18, 25, 47, 0.88);
        --line: rgba(184, 198, 255, 0.15);
        --text: #f4f6ff;
        --muted: #aab5d1;
        --violet: #b7a8ff;
        --cyan: #78e2dc;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        font-size: 17px;
    }

    .stApp {
        color: var(--text);
        background:
            radial-gradient(ellipse at 10% 0%, rgba(73, 111, 237, 0.22), transparent 34%),
            radial-gradient(ellipse at 85% 12%, rgba(150, 93, 255, 0.19), transparent 34%),
            radial-gradient(ellipse at 70% 90%, rgba(33, 177, 181, 0.10), transparent 32%),
            var(--bg);
        background-attachment: fixed;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #10172b, #090e1c);
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    .block-container {
        max-width: 1580px;
        padding: 2.3rem 3rem 4rem;
    }

    h1, h2, h3 {
        font-family: 'Manrope', sans-serif !important;
        letter-spacing: -0.04em;
        color: var(--text);
    }

    h1 {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
    }

    h2 {
        font-size: 2rem !important;
    }

    h3 {
        font-size: 1.5rem !important;
    }

    p, li {
        color: #d4dbef;
        font-size: 1.06rem;
        line-height: 1.75;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 2rem;
        color: #f0f2ff;
        font-family: 'Manrope', sans-serif;
        font-size: 1.2rem;
        font-weight: 800;
    }

    .brand-mark {
        display: grid;
        width: 44px;
        height: 44px;
        place-items: center;
        border-radius: 14px;
        color: #101629;
        font-size: 23px;
        background: linear-gradient(135deg, #c5baff, #72e2dc);
        box-shadow: 0 0 28px rgba(142, 127, 255, 0.28);
    }

    .eyebrow {
        color: #b7adff;
        font-size: 0.9rem;
        font-weight: 800;
        letter-spacing: 0.15em;
        text-transform: uppercase;
    }

    .hero-title {
        margin: 0.8rem 0 1rem;
        color: #f6f7ff;
        font-family: 'Manrope', sans-serif;
        font-size: clamp(3.2rem, 5.5vw, 5.5rem);
        font-weight: 800;
        letter-spacing: -0.075em;
        line-height: 1.04;
    }

    .hero-title span {
        color: #b7a8ff;
        background: linear-gradient(100deg, #c0b5ff, #77e4dc);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-copy {
        max-width: 850px;
        color: var(--muted);
        font-size: 1.2rem;
        line-height: 1.7;
    }

    .panel {
        height: 100%;
        padding: 22px;
        border: 1px solid var(--line);
        border-radius: 20px;
        background: linear-gradient(145deg, rgba(31, 42, 76, 0.82), rgba(15, 22, 43, 0.82));
        box-shadow: 0 20px 55px rgba(0, 0, 0, 0.18);
    }

    .panel-title {
        margin-bottom: 12px;
        color: #edf0ff;
        font-size: 1.08rem;
        font-weight: 800;
    }

    .workflow-item {
        padding: 8px 0;
        color: #b9c3dc;
        font-size: 1rem;
    }

    .section-label {
        margin: 1.7rem 0 0.7rem;
        color: #aeb9d5;
        font-size: 0.9rem;
        font-weight: 800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    div[data-baseweb="textarea"] textarea {
        min-height: 150px;
        border: 1px solid rgba(174, 190, 255, 0.2) !important;
        border-radius: 14px !important;
        background: rgba(5, 9, 19, 0.78) !important;
        color: #f5f7ff !important;
        font-size: 1.12rem !important;
        line-height: 1.65 !important;
    }

    div[data-baseweb="textarea"] textarea::placeholder {
        color: #8995b2 !important;
    }

    div.stButton > button,
    div[data-testid="stFormSubmitButton"] button,
    div[data-testid="stDownloadButton"] button {
        min-height: 50px;
        border: 1px solid rgba(184, 198, 255, 0.2);
        border-radius: 13px;
        color: #eff2ff;
        font-size: 1rem;
        font-weight: 700;
        background: rgba(25, 34, 61, 0.86);
        transition: transform 0.16s ease, filter 0.16s ease;
    }

    div.stButton > button:hover,
    div[data-testid="stDownloadButton"] button:hover {
        transform: translateY(-2px);
        border-color: rgba(183, 168, 255, 0.55);
        color: #ffffff;
        filter: brightness(1.1);
    }

    div[data-testid="stFormSubmitButton"] button {
        width: 100%;
        min-height: 58px;
        border: 0;
        color: #101629;
        font-size: 1.12rem;
        font-weight: 800;
        background: linear-gradient(100deg, #b6a8ff, #80e5df);
        box-shadow: 0 9px 30px rgba(123, 157, 255, 0.2);
    }

    div[data-testid="stFormSubmitButton"] button:hover {
        transform: translateY(-2px);
        color: #101629;
        filter: brightness(1.07);
    }

    [data-testid="stMetric"] {
        padding: 18px;
        border: 1px solid var(--line);
        border-radius: 16px;
        background: rgba(18, 25, 47, 0.78);
    }

    [data-testid="stMetricLabel"] {
        color: #aab5d1;
        font-size: 0.95rem;
    }

    [data-testid="stMetricValue"] {
        color: #f4f6ff;
        font-family: 'Manrope', sans-serif;
    }

    [data-testid="stTabs"] button {
        font-size: 1.05rem;
        font-weight: 700;
    }

    .empty-state {
        padding: 34px;
        border: 1px dashed rgba(184, 198, 255, 0.24);
        border-radius: 18px;
        color: #aab5d1;
        background: rgba(18, 25, 47, 0.45);
        text-align: center;
    }

    @media (max-width: 900px) {
        .block-container {
            padding: 1.5rem 1.2rem 3rem;
        }

        .hero-title {
            font-size: 3.2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if "topic" not in st.session_state:
    st.session_state.topic = ""

if "research_result" not in st.session_state:
    st.session_state.research_result = None


def set_example(example: str) -> None:
    st.session_state.topic = example


def clear_workspace() -> None:
    st.session_state.topic = ""
    st.session_state.research_result = None


with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-mark">✦</div>
            <div>Research Studio</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Your research team")
    st.caption("A focused workflow that searches, reads, writes, and reviews.")

    st.markdown("---")
    st.markdown("#### Research workflow")
    st.markdown("🔎 **Search** — Find relevant web sources")
    st.markdown("📖 **Read** — Extract useful page content")
    st.markdown("✍️ **Write** — Draft a structured report")
    st.markdown("🧭 **Review** — Critique the report")

    st.markdown("---")
    st.caption("Your API keys stay in your local environment variables.")
    st.button(
        "Clear workspace",
        use_container_width=True,
        on_click=clear_workspace,
    )


st.markdown('<div class="eyebrow">✦ Multi-agent research</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-title">Research with <span>receipts.</span></div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="hero-copy">
        Give your research team a question. It will search the web, read source
        pages, draft a report, and return a critique for review.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

left, right = st.columns([1.65, 0.8], gap="large")

with left:
    st.markdown('<div class="section-label">Start with a research question</div>', unsafe_allow_html=True)

    example_columns = st.columns(3)
    examples = [
        "How are AI agents being used in healthcare?",
        "What changed recently in EV battery technology?",
        "Recent advances in fraud detection",
    ]

    for column, example in zip(example_columns, examples):
        with column:
            st.button(
                example,
                key=f"example_{examples.index(example)}",
                use_container_width=True,
                on_click=set_example,
                args=(example,),
            )

    with st.form("research_form"):
        topic = st.text_area(
            "Research question",
            key="topic",
            placeholder=(
                "For example: Compare recent approaches to using AI agents "
                "in clinical documentation, including benefits, limitations, "
                "and evidence."
            ),
            label_visibility="collapsed",
        )

        submitted = st.form_submit_button("✦  Run research")

    if submitted:
        if not topic.strip():
            st.warning("Enter a research question first.")
        else:
            try:
                with st.spinner("Your research team is searching, reading, and writing..."):
                    st.session_state.research_result = run_research_pipeline(topic.strip())
            except Exception as error:
                st.error(f"Research run failed: {error}")


with right:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-title">What happens next</div>
            <div class="workflow-item">① &nbsp; Search for useful sources</div>
            <div class="workflow-item">② &nbsp; Read available source pages</div>
            <div class="workflow-item">③ &nbsp; Draft a structured report</div>
            <div class="workflow-item">④ &nbsp; Review the report with a critique</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


result = st.session_state.research_result

st.write("")
st.markdown("---")

if not result:
    st.markdown(
        """
        <div class="empty-state">
            <h3>Your workspace is ready</h3>
            <p>Your report and critique will appear here after your first research run.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    report = str(result.get("research_report", "No report was returned."))
    critique = str(result.get("critique", "No critique was returned."))

    st.markdown("## Research results")
    metric1, metric2 = st.columns(2)
    metric1.metric("Research report", "Ready")
    metric2.metric("Critique", "Ready")

    report_tab, critique_tab = st.tabs(["📄 Research report", "🧭 Critique"])

    with report_tab:
        st.markdown(report)
        st.download_button(
            "Download report",
            data=report,
            file_name="research_report.md",
            mime="text/markdown",
        )

    with critique_tab:
        st.markdown(critique)
        st.download_button(
            "Download critique",
            data=critique,
            file_name="research_critique.md",
            mime="text/markdown",
        )