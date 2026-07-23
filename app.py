import gradio as gr

def answer(question):
    if "안녕" in question:
        return "안녕하세요! GL.ai입니다."
    elif "OB" in question:
        return "OB는 코스 밖을 의미합니다.일반적으로는 1벌타가 있습니다."

    elif "벙커" in question:
        return "벙커에서는 샷할때를 제외하고 모래에 클럽이 절대 닿으면 안됩니다."

    elif "패널티 구역" in question:
        return "패널티 규역에서는 클럽을 지면에 대고 연습스윙을 해도 됩니다."
    elif "드롭" in question:
        return "드롭은 무릎 높이에서 해야 합니다."
    elif "언플레이어블(도저히 칠 수 없는 공)" in question:
        return "언플레이어블은 1벌타후 구제를 받을 수 있습니다."
    elif "러프에 박힌 공" in question:
        return "러프에 박힌 공은 무벌타 구제가 가능합니다."
    elif "그린" in question :
        return "그린에서는 볼마크로공위치를 표시한 다음 공을 닦고 플레이가 가능합니다."
    elif "개발자" in question:
        return "GL.ai의 개발자는 골프견입니다."
    else :
        return "아직 배우지 못한 질문입니다."


theme = gr.themes.Soft()
css = """
body {
    background:  #DFF6FF;
    }
    """

demo = gr.Interface(
    theme=theme,
    css=css,
    fn=answer,
    inputs="text",
    outputs="text",
    title="Gl.ai",
    description="GL.ai 입니다.",
    submit_btn="질문하기",
    clear_btn="초기화",



)

improt os

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("port", 7860))
)
