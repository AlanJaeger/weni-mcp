import os
import json

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("weni-insights")

WENI_BASE_URL = "https://insights-engine.weni.ai/v1"
WENI_API_TOKEN = os.getenv("WENI_API_TOKEN", "")


@mcp.tool()
async def get_conversation_totals(
    project_uuid: str,
    start_date: str,
    end_date: str,
) -> str:
    """Busca métricas totais de conversas de um projeto Weni em um período.

    Retorna total de conversas, quantas foram resolvidas,
    não resolvidas e transferidas para atendimento humano,
    com valores absolutos e percentuais.

    Args:
        project_uuid: UUID do projeto Weni.
        start_date: Data de início no formato YYYY-MM-DD.
        end_date: Data de fim no formato YYYY-MM-DD.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{WENI_BASE_URL}/metrics/conversations/totals/",
            params={
                "project_uuid": project_uuid,
                "start_date": start_date,
                "end_date": end_date,
            },
            headers={"Authorization": f"Bearer {WENI_API_TOKEN}"},
        )
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)


if __name__ == "__main__":
    mcp.run()
