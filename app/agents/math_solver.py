import shutil
import os
from app.workflow.math_graph import build_graph
from app.hitl.hitl_manager import handle_hitl
from app.multimodal.ocr import extract_text_from_image
from app.multimodal.speech_to_text import transcribe_audio

graph = build_graph()

def solve_math_problem(question: str):

    result = graph.invoke({
        "question": question
    })

    final_output = handle_hitl(
        question,
        result["parsed_problem"],
        result["solution"],
        result["verification"]
    )

    return {
        "question": question,
        "solution": final_output["symbolic_solution"],
        "explanation": final_output["explanation"],
        "verification": result["verification"]
    }
