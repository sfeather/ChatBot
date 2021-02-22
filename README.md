# ChatBot
ChatBot is an assistant that helps you navigate on internet (youtube, wikipedia, google) and answers your questions about different topics.

KNOWN PROBLEMS!

For the error "ModuleNotFoundError: No module named 'en_core_web_sm'" after installing spaCy:
- In venv/lib/chatterbot/languages.py add to class "class ENG" this: ISO_639_1 = 'en_core_web_sm'

For the warning "ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map":
- In /usr/share/alsa/alsa.conf comment the following lines:
                pcm.rear cards.pcm.rear
                pcm.center_lfe cards.pcm.center_lfe
                pcm.side cards.pcm.side
