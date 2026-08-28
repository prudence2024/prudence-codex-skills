# Voice Audio Operational Playbook

Use this playbook for speech-to-text, text-to-speech, AI voice-over, realtime voice, local audio models, hosted APIs, and voice interface planning.

## Inputs

- Use case: dictation, command interface, voice agent, narration, accessibility, transcription, translation, or media generation.
- Latency target, quality target, languages/accents, privacy constraints, device/hardware, budget, offline need, and licensing requirements.
- Current stack, provider candidates, local model options, and data handling constraints.

## Procedure

1. Classify the capability: STT, TTS, realtime conversation, voice-over, voice cloning, audio analysis, or local inference.
2. Identify constraints: latency, streaming, accuracy, privacy, consent, retention, noise environment, hardware, cost, and reliability.
3. Decide local vs hosted:
   - Local for privacy/offline/control when hardware and maintenance are acceptable.
   - Hosted API for quality, scale, maintenance, and streaming when data policy allows.
4. Use research-intelligence for current provider/model facts and package-intelligence for SDK adoption.
5. Design data flow: capture, consent, buffering, upload, processing, storage, deletion, logs, and error handling.
6. Plan fallback: text input, retry, lower-quality model, queue, manual upload, or disabled voice feature.
7. Verify representative samples: quiet/noisy audio, accents/languages, long input, interruptions, silence, invalid file, network failure, and cancellation.
8. Measure latency end to end, not just provider response time.
9. Check licensing for voices, generated audio, datasets, model weights, and commercial use.
10. Report risks and untested environments.

## Decision Points

- Do not process private audio without explicit authorization.
- Do not lock ADE to one provider without current evidence and an approved architecture decision.
- Do not use voice cloning or biometric-like features without explicit consent and legal/privacy review.
- If voice is not essential, preserve a non-audio workflow.

## Failure Modes To Break

- Latency too high for realtime use.
- Audio retained or logged unexpectedly.
- No fallback when microphone permission is denied.
- Poor handling of silence, noise, accents, or long files.
- Licensing does not permit intended commercial use.
- Provider outage disables core workflow without recovery.

## Verification

```text
CAPABILITY:
LOCAL_OR_HOSTED:
PROVIDER/MODEL OPTIONS:
PRIVACY/CONSENT:
LATENCY TEST:
QUALITY TEST:
FALLBACK:
LICENSING:
EVIDENCE:
```

## Related Skills

- research-intelligence for current model/provider facts.
- package-intelligence for SDK/package adoption.
- security for privacy and data handling.
- system-breaker for failure and abuse testing.
