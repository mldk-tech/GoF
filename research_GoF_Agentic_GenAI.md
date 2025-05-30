# מחקר יישום דפוסי GoF במערכות Agentic GenAI

מסמך זה מפרט מתודולוגיה לחקר ויישום דפוסי התכנון של Gang of Four (GoF) בסביבות Agentic GenAI. המיקוד הוא בשילוב דפוסי תכנון קלאסיים עם סוכנים המונעים על ידי מודלי שפה גדולים (LLMs) וכלי עזר משלימים.

## 1. מיפוי אובייקטים מרכזיים במערכת

* **סוכנים (Agents)** – יחידות עצמאיות לביצוע משימות.
* **מודלי שפה (LLMs)** – המנוע הקוגניטיבי של הסוכנים.
* **כלים/פונקציות** – ממשקים לשירותים חיצוניים וליכולות מערכתיות.
* **מודולי זיכרון** – ניהול מצב מתמשך וזיכרון משימות.
* **מתכננים/אסטרטגיות** – קבלת החלטות ותכנון צעדים.
* **קונטקסטים/סשנים** – מצבים המגדירים את התנהגות הסוכנים.

## 2. דפוסי יצירה (Creational)

### Factory Method / Abstract Factory
יצירת סוכנים או כלים בהתאם לסוג משימה ולדרישות המשתמש. מאפשר החלפה קלה של LLM או כלי ללא שינוי בקוד הקורא.
```python
class AgentFactory:
    def create_agent(self, agent_type: str):
        if agent_type == "planner":
            return PlannerAgent()
        if agent_type == "executor":
            return ExecutorAgent()
        raise ValueError("unknown type")
```

### Singleton
ניהול רכיבים מערכתיים בעלי מופע יחיד, כגון מנהל תצורה או לוגים.
```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load()
        return cls._instance

    def load(self):
        self.settings = {}
```

### Builder
הרכבה הדרגתית של פרומפטים או סוכנים עם יכולות מרובות.
```python
class PromptBuilder:
    def __init__(self):
        self.parts = []
    def add_instruction(self, text):
        self.parts.append(text)
        return self
    def build(self):
        return "\n".join(self.parts)
```

## 3. דפוסי מבנה (Structural)

### Adapter
שכבת התאמה בין הסוכן לממשקי API חיצוניים בעלי חתימות שונות.
```python
class SearchAdapter:
    def __init__(self, api_client):
        self.api_client = api_client
    def search(self, query):
        return self.api_client.do_search(q=query)
```

### Composite
הרכבת סוכן מורכב מסוכנים פשוטים יותר ופניה אליו כאל יחידה אחת.
```python
class CompositeAgent:
    def __init__(self, agents):
        self.agents = agents
    def run(self, task):
        for agent in self.agents:
            agent.run(task)
```

### Decorator
הוספת תכונות לסוכן קיים ללא שינוי בקוד המקורי.
```python
class LoggingAgent:
    def __init__(self, agent):
        self.agent = agent
    def run(self, task):
        print("start", task)
        result = self.agent.run(task)
        print("end", task)
        return result
```

### Facade
מתן ממשק אחיד לפעולות מורכבות של כמה סוכנים וכלים.
```python
class ProjectBot:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
    def handle_request(self, req):
        plan = self.planner.plan(req)
        return self.executor.execute(plan)
```

## 4. דפוסי התנהגות (Behavioral)

### Chain of Responsibility
טיפול בבקשה העוברת בשרשרת סוכנים עד למציאת טיפול מתאים.
```python
class IntentAgent:
    def __init__(self, next_agent=None):
        self.next_agent = next_agent
    def handle(self, req):
        if self.can_handle(req):
            return self.process(req)
        if self.next_agent:
            return self.next_agent.handle(req)
```

### Observer
עדכון סוכנים על אירועים במערכת בצורה אסינכרונית.
```python
class EventBus:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, fn):
        self.subscribers.append(fn)
    def publish(self, event):
        for fn in self.subscribers:
            fn(event)
```

### Strategy
בחירה דינמית של אלגוריתם או גישה בהתאם למצב.
```python
class SearchStrategy:
    def search(self, query):
        raise NotImplementedError
class ApiSearch(SearchStrategy):
    def search(self, query):
        return external_api(query)
class LocalSearch(SearchStrategy):
    def search(self, query):
        return local_index.lookup(query)
```

### Mediator
רכיב מתווך המנהל תקשורת בין סוכנים שונים.
```python
class TaskCoordinator:
    def __init__(self, agents):
        self.agents = agents
    def dispatch(self, task):
        for agent in self.agents:
            agent.notify(task)
```

### State
שינוי התנהגות סוכן לפי מצבו הפנימי.
```python
class AgentState:
    def handle(self, agent, data):
        raise NotImplementedError
class WaitingState(AgentState):
    def handle(self, agent, data):
        agent.buffer.append(data)
        if agent.ready():
            agent.state = ProcessingState()
class ProcessingState(AgentState):
    def handle(self, agent, data):
        agent.process(data)
```

## 5. ניתוח יתרונות וחסרונות

יש לאזן בין מורכבות היתר שמוסיפים דפוסים לבין גמישות ותחזוקתיות. במערכות Agentic GenAI דפוסים מסוימים (כגון Mediator או Composite) מסייעים בבניית מערך סוכנים מודולרי, אך יש לשים לב שלא להכביד על המערכת במקרים פשוטים.

## 6. המלצות מעשיות

1. **להתחיל קטן** – לבנות אבות טיפוס של סוכנים עם מעט דפוסים, ורק לאחר מכן להרחיב.
2. **בחירה מושכלת של דפוסים** – לא כל דפוס מתאים לכל מצב; יש לבחור בהתאם לאופי המשימה.
3. **הפרדה ברורה בין לוגיקה עסקית לתשתיות** – דפוסי מבנה כמו Facade ו-Adapter עוזרים בכך.
4. **ניטור ולוגינג** – מומלץ לשלב דפוס Decorator לצורכי מעקב וניטור.

## 7. סיכום

שילוב דפוסי GoF במערכות Agentic GenAI מחזק את מבנה המערכת ומאפשר גמישות ארוכת טווח. שילוב זה מתאפשר בשימוש ב-Python ובספריות סוכנים קיימות כמו LangChain או AutoGen, תוך שימת דגש על תהליכי יצירה, מבנה והתנהגות של סוכנים וכלים.
