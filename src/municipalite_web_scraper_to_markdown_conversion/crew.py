from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerplyWebpageToMarkdownTool

@CrewBase
class MunicipaliteWebScraperToMarkdownConversionCrew():
    """MunicipaliteWebScraperToMarkdownConversion crew"""

    @agent
    def website_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['website_scraper'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def markdown_converter(self) -> Agent:
        return Agent(
            config=self.agents_config['markdown_converter'],
            tools=[SerplyWebpageToMarkdownTool()],
        )


    @task
    def scrape_website_task(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_website_task'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def convert_to_markdown_task(self) -> Task:
        return Task(
            config=self.tasks_config['convert_to_markdown_task'],
            tools=[SerplyWebpageToMarkdownTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the MunicipaliteWebScraperToMarkdownConversion crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
