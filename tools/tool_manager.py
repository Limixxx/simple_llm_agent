from abc import ABC, abstractmethod
import time


def timeit(func):
    """Decorator to measure and print the execution time of a function."""

    def timed(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds. ⏱️")
        return result

    return timed


class BaseTool(ABC):
    """Abstract base class for all tools"""

    def __init__(self, name, description):
        self._name = name.lower()  # Store the name in lowercase for consistency
        self._description = description
        Tools.regist_tool(self)

    @property
    def name(self):
        """Getter for tool name."""
        return self._name

    @property
    def description(self):
        """Getter for tool description."""
        return self._description

    @abstractmethod
    def execute(self, query):
        """Each tool must implement its own `use` method"""
        pass


class Tools:
    """Tool的管理类"""
    _tools = {}

    @staticmethod
    def regist_tool(tool: BaseTool):
        """注册工具"""
        Tools._tools[tool.name.lower()] = tool

    @staticmethod
    def get_tool(name: str) -> BaseTool:
        """获取工具"""
        return Tools._tools.get(name)

    @staticmethod
    def get_tools() -> list:
        """获取工具列表"""
        return list(Tools._tools.values())

    @staticmethod
    @timeit
    def execute(name, query):
        """执行工具"""
        return Tools._tools[name].execute(query)


if __name__ == "__main__":
    class Test(BaseTool):

        def __init__(self):
            super().__init__("test", "test")

        def execute(self, query):
            return query


    test = Test()
    for tool in Tools.get_tools():
        print(tool.name)
