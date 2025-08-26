from typing import TypedDict, Annotated , Literal , Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name='gpt-3.5-turbo-1106', temperature=0)

class summary(TypedDict):
    key_themes : Annotated[list[str],'A list of key themes in the review']
    summary : Annotated[str,'A brief summary of the review']
    sentiment : Annotated[Literal['positive','negative','neutral'],'The sentiment of the review']
    pros : Annotated[Optional[list[str]],'A list of pros mentioned in the review']  
    cons : Annotated[Optional[list[str]],'A list of cons mentioned in the review']
    rating : Annotated[Optional[float],'The rating given in the review (1-5)']
    

structured_output = model.with_structured_output(summary)

review = """
I recently got the Samsung Galaxy S25 Ultra, and it truly feels like a powerhouse. The massive AMOLED display with 2K resolution and 144Hz refresh rate is breathtaking — colors pop, and outdoor visibility is unmatched thanks to its 3000-nit brightness. Performance is equally impressive; the Snapdragon Gen 4 handles gaming, multitasking, and heavy apps with ease, making it one of the smoothest phones I’ve ever used.

The camera system is outstanding, especially the 200MP main sensor and 10x optical zoom, which capture incredible detail in both daylight and low-light. Night mode feels like a genuine leap forward, and Samsung’s AI photo editing tools are surprisingly useful for quick fixes. Add in the S Pen, stereo speakers, and Samsung DeX, and it feels more like a productivity device than just a phone.

That said, it’s not perfect. The phone is bulky and heavy, and charging is still limited to 45W, which feels slow compared to rivals. Some AI features feel more like gimmicks, and the lack of a charger in the box is disappointing at this price point.

Overall, the S25 Ultra is a true flagship: premium design, unbeatable display, powerful cameras, and long software support. It’s expensive, but if you want the **best Android experience** available right now, this phone delivers.

"""

result = structured_output.invoke(review)

print(result['cons'])
