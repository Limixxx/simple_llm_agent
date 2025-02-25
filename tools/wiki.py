from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from tool_manager import BaseTool


class Wiki(BaseTool):
    """Wikipedia是一个多语言免费在线百科全书，由称为Wikipedians的志愿者社区通过开放协作并使用名为MediaWiki的基于wiki的编辑系统编写和维护。
Wikipedia是历史上最大、阅读量最大的参考著作。"""

    name = "wiki"
    description = ""

    def __init__(self):
        super().__init__(self.name, self.description)
        self.wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

    def execute(self, query: str):
        """Fetches summary information from Wikipedia for a given topic."""
        if not query:
            raise ValueError("Query cannot be empty.")

        try:
            result = self.wiki.run(query)
            return result
        except Exception:
            return "An error occurred while searching Wikipedia."


if __name__ == "__main__":
    from tool_manager import Tools

    wiki = Wiki()
    print(Tools.execute(wiki.name, "HUNTER X HUNTER"))
