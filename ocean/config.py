import os
from pathlib import Path

from haystack.utils import Secret

HERE = Path(__file__).resolve().parent.parent
persist_path = HERE / "persist_path"

# data_urls = [
#     "https://centreforeffectivealtruism.notion.site/In-Depth-EA-Program-Syllabus-54302c8718cb4358b3d971309b17d596",
#     "https://centreforeffectivealtruism.notion.site/Week-1-Introductions-53e078a0a6734341835b324d6e759dce",
#     "https://centreforeffectivealtruism.notion.site/Week-2-What-do-you-value-c87e084e358a40cfb08326b861e96367",
#     "https://centreforeffectivealtruism.notion.site/Week-3-How-do-you-form-beliefs-76f6b555bbdd4b5fb6febf912bffb533",
#     "https://centreforeffectivealtruism.notion.site/Heavy-Tailed-Impact-7be6e3b8448e4731a49d424f0917027f",
#     "https://centreforeffectivealtruism.notion.site/Decision-Theory-0431b15e8cf54e459ee41d8c93eec853",
#     "https://centreforeffectivealtruism.notion.site/Uncertainty-7bfe471cb75a413898b72b4f1619133f",
#     "https://centreforeffectivealtruism.notion.site/Using-Forecasting-Tools-687349c0092c4922bb43fd01c49ae257",
#     "https://centreforeffectivealtruism.notion.site/Global-Catastrophic-Biorisks-1ee8aba8933a42a3808e9b31d7933c31",
#     "https://centreforeffectivealtruism.notion.site/Global-Health-Development-fa0eb59fbab444e2b6aed679daf4bcf2",
#     "https://centreforeffectivealtruism.notion.site/Nonhuman-Animals-Farmed-Wild-and-Future-Animals-69581205a4e3475caffbcbbd780493fe",
#     "https://centreforeffectivealtruism.notion.site/Existential-Risk-from-Artificial-Intelligence-c4f5f3a41dac452bba6f63fcfdf3b83a",
#     "https://centreforeffectivealtruism.notion.site/Limits-of-Evidence-and-Cluelessness-25ef8d9d6480406784d3f6685f1468be",
#     "https://centreforeffectivealtruism.notion.site/Community-Building-for-Effective-Altruism-408ebebe7bcf42aa81ef7cfffa388e8e",
#     "https://centreforeffectivealtruism.notion.site/Something-Else-376810cf77d34d90bb777ff3289fe1ea",
#     "https://centreforeffectivealtruism.notion.site/Week-8-Next-Steps-c89e3809cb284ad79d2e5140edf46a64",
# ]

data_urls = [
    "https://en.wikipedia.org/wiki/Octopus",
    "https://en.wikipedia.org/wiki/Cuttlefish",
    "https://en.wikipedia.org/wiki/Cephalopod",
]


anthropic_api_key = Secret.from_env_var("ANTHROPIC_API_KEY")
