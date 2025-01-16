from dotenv import load_dotenv
import asyncio
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import (
    openai,
    silero,
)
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
    llm,
)

load_dotenv()

# settings
from settings import (
    SYSTEM_MESSAGE
)

SYSTEM_MESSAGE = SYSTEM_MESSAGE.format(
    client_name="Jarib", 
    store_manager_name="Dorian",
    store_location="W Lake Mead Blvd"
)

async def entrypoint(ctx: JobContext):
    context = llm.ChatContext().append(
        role="system",
        text=SYSTEM_MESSAGE,
    )

    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=context
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    assistant.start(
        room=ctx.room,
    )

    await asyncio.sleep(1)

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(entrypoint_fnc=entrypoint)
    )

    
