import json
import random
import time
from datetime import datetime
from typing import List, Dict, Optional


class Question:
    def __init__(self, text: str, options: List[str], correct_answer: str, question_type: str = "multiple_choice"):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.question_type = question_type

    def validate_answer(self, user_answer: str) -> bool:
        """Check if the user's answer is correct"""
        return user_answer.lower() == self.correct_answer.lower()

    def to_dict(self) -> Dict:
        """Convert question to dictionary for storage"""
        return {
            "text": self.text,
            "options": self.options,
            "correct_answer": self.correct_answer,
            "question_type": self.question_type
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create question from dictionary"""
        return cls(
            text=data["text"],
            options=data["options"],
            correct_answer=data["correct_answer"],
            question_type=data.get("question_type", "multiple_choice")
        )


class Quiz:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.questions: List[Question] = []
        self.created_at = datetime.now()
        self.time_limit: Optional[int] = None  # in seconds

    def add_question(self, question: Question):
        """Add a question to the quiz"""
        self.questions.append(question)

    def set_time_limit(self, minutes: int):
        """Set time limit for the quiz in minutes"""
        self.time_limit = minutes * 60

    def shuffle_questions(self):
        """Randomize the order of questions"""
        random.shuffle(self.questions)

    def to_dict(self) -> Dict:
        """Convert quiz to dictionary for storage"""
        return {
            "title": self.title,
            "description": self.description,
            "questions": [q.to_dict() for q in self.questions],
            "created_at": self.created_at.isoformat(),
            "time_limit": self.time_limit
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create quiz from dictionary"""
        quiz = cls(
            title=data["title"],
            description=data.get("description", "")
        )
        quiz.created_at = datetime.fromisoformat(data["created_at"])
        quiz.time_limit = data.get("time_limit")
        quiz.questions = [Question.from_dict(q) for q in data["questions"]]
        return quiz


class QuizResult:
    def __init__(self, quiz_title: str):
        self.quiz_title = quiz_title
        self.score = 0
        self.total_questions = 0
        self.answers: List[Dict] = []
        self.completed_at = datetime.now()
        self.time_taken: Optional[float] = None  # in seconds

    def add_answer(self, question: Question, user_answer: str, is_correct: bool):
        """Record an answer"""
        self.answers.append({
            "question": question.text,
            "user_answer": user_answer,
            "correct_answer": question.correct_answer,
            "is_correct": is_correct
        })
        self.total_questions += 1
        if is_correct:
            self.score += 1

    def calculate_percentage(self) -> float:
        """Calculate score percentage"""
        return (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0

    def to_dict(self) -> Dict:
        """Convert result to dictionary for storage"""
        return {
            "quiz_title": self.quiz_title,
            "score": self.score,
            "total_questions": self.total_questions,
            "percentage": self.calculate_percentage(),
            "answers": self.answers,
            "completed_at": self.completed_at.isoformat(),
            "time_taken": self.time_taken
        }


class QuizManager:
    def __init__(self):
        self.quizzes: List[Quiz] = []
        self.results: List[QuizResult] = []
        self.load_data()

    def create_quiz(self, title: str, description: str = "") -> Quiz:
        """Create a new quiz"""
        quiz = Quiz(title, description)
        self.quizzes.append(quiz)
        return quiz

    def find_quiz(self, title: str) -> Optional[Quiz]:
        """Find quiz by title"""
        for quiz in self.quizzes:
            if quiz.title.lower() == title.lower():
                return quiz
        return None

    def delete_quiz(self, title: str) -> bool:
        """Delete a quiz"""
        quiz = self.find_quiz(title)
        if quiz:
            self.quizzes.remove(quiz)
            return True
        return False

    def take_quiz(self, quiz: Quiz) -> QuizResult:
        """Take a quiz and return results"""
        print(f"\n=== {quiz.title} ===")
        print(quiz.description)

        if quiz.time_limit:
            print(f"\nTime limit: {quiz.time_limit // 60} minutes")

        result = QuizResult(quiz.title)
        start_time = time.time()

        if quiz.time_limit:
            time_left = quiz.time_limit

        for i, question in enumerate(quiz.questions, 1):
            print(f"\nQuestion {i}/{len(quiz.questions)}")
            print(question.text)

            if question.question_type == "multiple_choice":
                for j, option in enumerate(question.options, 1):
                    print(f"{j}. {option}")
                user_answer = input("Your answer (number): ")

                # Validate input
                while not user_answer.isdigit() or int(user_answer) not in range(1, len(question.options) + 1):
                    print("Invalid input. Please enter the number of your choice.")
                    user_answer = input("Your answer (number): ")

                selected_option = question.options[int(user_answer) - 1]
                is_correct = question.validate_answer(selected_option)

            elif question.question_type == "true_false":
                user_answer = input("Your answer (True/False): ").lower()
                while user_answer not in ["true", "false", "t", "f"]:
                    print("Invalid input. Please enter True or False.")
                    user_answer = input("Your answer (True/False): ").lower()

                # Normalize to "True" or "False"
                normalized_answer = "true" if user_answer in ["true", "t"] else "false"
                is_correct = question.validate_answer(normalized_answer)

            elif question.question_type == "short_answer":
                user_answer = input("Your answer: ")
                is_correct = question.validate_answer(user_answer)

            result.add_answer(question, user_answer, is_correct)

            if quiz.time_limit:
                elapsed = time.time() - start_time
                time_left = quiz.time_limit - elapsed
                if time_left <= 0:
                    print("\nTime's up!")
                    break
                print(f"Time remaining: {int(time_left // 60)}:{int(time_left % 60):02d}")

        result.time_taken = time.time() - start_time
        self.results.append(result)
        return result

    def review_result(self, result: QuizResult):
        """Display quiz results"""
        print(f"\n=== Quiz Results: {result.quiz_title} ===")
        print(f"Score: {result.score}/{result.total_questions}")
        print(f"Percentage: {result.calculate_percentage():.1f}%")

        if result.time_taken:
            mins, secs = divmod(result.time_taken, 60)
            print(f"Time taken: {int(mins)}:{int(secs):02d}")

        print("\n=== Question Review ===")
        for i, answer in enumerate(result.answers, 1):
            print(f"\nQ{i}: {answer['question']}")
            print(f"Your answer: {answer['user_answer']}")
            print(f"Correct answer: {answer['correct_answer']}")
            print("✅ Correct" if answer["is_correct"] else "❌ Incorrect")

    def get_quiz_history(self, quiz_title: str = None) -> List[QuizResult]:
        """Get quiz results, optionally filtered by quiz title"""
        if quiz_title:
            return [r for r in self.results if r.quiz_title.lower() == quiz_title.lower()]
        return self.results

    def save_data(self):
        """Save quizzes and results to file"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "results": [r.to_dict() for r in self.results]
        }
        with open("quiz_data.json", "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        """Load quizzes and results from file"""
        try:
            with open("quiz_data.json", "r") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
                self.results = [
                    QuizResult(r["quiz_title"]) for r in data["results"]
                ]  # Simplified loading of results
        except (FileNotFoundError, json.JSONDecodeError):
            self.quizzes = []
            self.results = []


def create_question_interactive() -> Question:
    """Interactive question creation"""
    print("\n=== Create New Question ===")
    question_type = input("Question type (multiple_choice/true_false/short_answer): ").lower()

    while question_type not in ["multiple_choice", "true_false", "short_answer", "mc", "tf", "sa"]:
        print("Invalid question type. Please choose multiple_choice, true_false, or short_answer")
        question_type = input("Question type: ").lower()

    # Normalize question type
    if question_type in ["mc", "multiple_choice"]:
        question_type = "multiple_choice"
    elif question_type in ["tf", "true_false"]:
        question_type = "true_false"
    else:
        question_type = "short_answer"

    text = input("Question text: ")

    if question_type == "multiple_choice":
        options = []
        print("Enter options (leave blank to finish):")
        while True:
            option = input(f"Option {len(options) + 1}: ")
            if not option:
                if len(options) < 2:
                    print("Please enter at least 2 options")
                    continue
                break
            options.append(option)

        correct = input("Correct option number: ")
        while not correct.isdigit() or int(correct) not in range(1, len(options) + 1):
            print(f"Please enter a number between 1 and {len(options)}")
            correct = input("Correct option number: ")

        correct_answer = options[int(correct) - 1]

    elif question_type == "true_false":
        correct = input("Correct answer (True/False): ").lower()
        while correct not in ["true", "false", "t", "f"]:
            print("Please enter True or False")
            correct = input("Correct answer (True/False): ").lower()

        correct_answer = "true" if correct in ["true", "t"] else "false"
        options = ["True", "False"]

    else:  # short_answer
        correct_answer = input("Correct answer: ")
        options = []

    return Question(text, options, correct_answer, question_type)


def main_menu():
    print("\n=== Quiz Application ===")
    print("1. Create new quiz")
    print("2. Take a quiz")
    print("3. Review quiz results")
    print("4. View quiz history")
    print("5. Delete a quiz")
    print("6. Exit")


def main():
    manager = QuizManager()

    while True:
        main_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\n=== Create New Quiz ===")
            title = input("Quiz title: ")
            description = input("Quiz description (optional): ")

            quiz = manager.create_quiz(title, description)

            # Set time limit
            time_limit = input("Time limit in minutes (leave blank for no limit): ")
            if time_limit:
                quiz.set_time_limit(int(time_limit))

            # Add questions
            while True:
                question = create_question_interactive()
                quiz.add_question(question)

                if input("\nAdd another question? (y/n): ").lower() != "y":
                    break

            # Shuffle questions if desired
            if input("Shuffle questions in this quiz? (y/n): ").lower() == "y":
                quiz.shuffle_questions()

            manager.save_data()
            print(f"\nQuiz '{title}' created successfully!")

        elif choice == "2":
            if not manager.quizzes:
                print("\nNo quizzes available. Please create a quiz first.")
                continue

            print("\nAvailable quizzes:")
            for i, quiz in enumerate(manager.quizzes, 1):
                print(f"{i}. {quiz.title} - {len(quiz.questions)} questions")

            selection = input("\nEnter quiz number to take: ")
            while not selection.isdigit() or int(selection) not in range(1, len(manager.quizzes) + 1):
                print(f"Please enter a number between 1 and {len(manager.quizzes)}")
                selection = input("Enter quiz number to take: ")

            quiz = manager.quizzes[int(selection) - 1]
            result = manager.take_quiz(quiz)
            manager.save_data()

            print("\nQuiz completed!")
            manager.review_result(result)

        elif choice == "3":
            if not manager.results:
                print("\nNo quiz results available.")
                continue

            print("\nRecent quiz results:")
            for i, result in enumerate(manager.results[-5:][::-1], 1):
                print(f"{i}. {result.quiz_title} - {result.score}/{result.total_questions} - {result.completed_at}")

            selection = input("\nEnter result number to review (or leave blank to go back): ")
            if not selection:
                continue

            while not selection.isdigit() or int(selection) not in range(1, len(manager.results[-5:]) + 1):
                print(f"Please enter a number between 1 and {len(manager.results[-5:])}")
                selection = input("Enter result number to review: ")

            result = manager.results[-int(selection)]
            manager.review_result(result)

        elif choice == "4":
            if not manager.results:
                print("\nNo quiz history available.")
                continue

            print("\n=== Quiz History ===")
            for quiz in manager.quizzes:
                results = manager.get_quiz_history(quiz.title)
                if results:
                    avg_score = sum(r.calculate_percentage() for r in results) / len(results)
                    print(f"\n{quiz.title} - {len(results)} attempts")
                    print(f"Average score: {avg_score:.1f}%")
                    print(f"Highest score: {max(r.calculate_percentage() for r in results):.1f}%")
                    print(f"Lowest score: {min(r.calculate_percentage() for r in results):.1f}%")

        elif choice == "5":
            if not manager.quizzes:
                print("\nNo quizzes available to delete.")
                continue

            print("\nAvailable quizzes:")
            for i, quiz in enumerate(manager.quizzes, 1):
                print(f"{i}. {quiz.title}")

            selection = input("\nEnter quiz number to delete: ")
            while not selection.isdigit() or int(selection) not in range(1, len(manager.quizzes) + 1):
                print(f"Please enter a number between 1 and {len(manager.quizzes)}")
                selection = input("Enter quiz number to delete: ")

            quiz = manager.quizzes[int(selection) - 1]
            if manager.delete_quiz(quiz.title):
                manager.save_data()
                print(f"\nQuiz '{quiz.title}' deleted successfully!")
            else:
                print("\nFailed to delete quiz.")

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()