import re
import random

class KJ_Eliza:
    def __init__(self):
        self.name = "ELIZA"
        self.last_topic = None

    def KJ_greet(self):
        return "Hello. How are you feeling today?"

    def KJ_patterns(self):
        return [
            (
                r"\b(hello|hi|hey)\b",
                [
                    "Hello. What would you like to discuss?",
                    "Hello. How are you feeling today?"
                ]
            ),
            (
                r"\b(sorry|apologize)\b",
                [
                    "There is no need to apologize.",
                    "What makes you feel sorry?"
                ]
            ),
            (
                r"\b(always|never)\b",
                [
                    "Can you think of a specific example?",
                    "Are you sure that is always the case?"
                ]
            ),
            (
                r"\b(dream|dreamed|dreamt)\b",
                [
                    "What does that dream mean to you?",
                    "Do you often remember your dreams?"
                ]
            ),
            (
                r"\b(computer|machine|robot)\b",
                [
                    "Why are you interested in computers?",
                    "Do machines worry you?"
                ]
            ),
            (
                r"\b(friend|friends)\b",
                [
                    "Tell me more about your friends.",
                    "How important are your friendships to you?"
                ]
            )
        ]

    def KJ_reflect(self, text):
        replacements = {
            "i": "you",
            "me": "you",
            "my": "your",
            "mine": "yours",
            "am": "are",
            "you": "I",
            "your": "my",
            "yours": "mine"
        }

        words = re.findall(r"\w+|[^\w\s]", text.lower())
        reflected = []

        for word in words:
            reflected.append(replacements.get(word, word))

        result = " ".join(reflected)
        return re.sub(r"\s+([.,!?])", r"\1", result)

    def KJ_respond(self, message):
        message = message.strip()

        if not message:
            return "Please say something."

        if re.search(r"\b(mother|father|family)\b", message, re.IGNORECASE):
            self.last_topic = "family"

        if re.fullmatch(
            r"(yes|no|maybe|it is|it's (good|bad|great|terrible|fine))[.!?]?",
            message,
            re.IGNORECASE
        ):
            if self.last_topic == "family":
                return "How does that relate to your family?"

        for pattern, answers in self.KJ_patterns():
            if re.search(pattern, message, re.IGNORECASE):
                return random.choice(answers)

        match = re.fullmatch(
            r"I feel (.+?)[.!?]?",
            message,
            re.IGNORECASE
        )

        if match:
            feeling = match.group(1)
            return f"Why do you feel {feeling}?"

        if re.search(r"\bmother\b", message, re.IGNORECASE):
            return "Tell me more about your family."

        if re.search(r"\bfather\b", message, re.IGNORECASE):
            return "How is your relationship with your father?"

        if re.search(r"\bfamily\b", message, re.IGNORECASE):
            return "What does your family mean to you?"

        match = re.fullmatch(
            r"I (want|need|think|believe) (.+?)[.!?]?",
            message,
            re.IGNORECASE
        )

        if match:
            verb = match.group(1).lower()
            reflected = self.KJ_reflect(match.group(2))

            if verb == "want":
                return f"Why do you want {reflected}?"

            if verb == "need":
                return f"Why do you need {reflected}?"

            return f"What makes you {verb} that {reflected}?"

        responses = [
            "Please tell me more.",
            "Can you elaborate on that?",
            "Why do you say that?",
            "How does that make you feel?",
            "What comes to mind when you say that?",
            "Let's explore that further."
        ]

        return random.choice(responses)
