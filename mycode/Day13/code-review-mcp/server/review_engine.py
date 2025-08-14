import subprocess
from pydantic import BaseModel
from typing import List


class CodeReviewRequest(BaseModel):
    code: str
    language: str
    requirements: List[str] = []


class ClaudeCodeReviewer:
    def __init__(self):
        self.prompt_template = """
        [System] You are a senior {language} engineer reviewing GitLab code.
        Analyze for: {requirements}

        [Code]
        {code}

        [Output Format]
        - Security: /10
        - Performance: /10
        - Maintainability: /10
        - Summary: 3 bullet points
        """

    def analyze(self, request: CodeReviewRequest) -> str:
        prompt = self.prompt_template.format(
            language=request.language,
            requirements=", ".join(request.requirements),
            code=request.code
        )

        # Local Claude execution
        cmd = f"ollama run claude3-sonnet '{prompt}'"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        return result.stdout

# FastAPI would wrap this (omitted for brevity)