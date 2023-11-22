from chat import chat
from whisper import voice_to_text
from voicevox import text_to_voice

EXIT_PHRASE = 'exit'

def main():
    messages = [
        {'role': 'system', 'content': '\
            あなたの名前は「春日部つむぎ」です。\
            すべてに日本語で答えてください。\
            チャットであることを強く意識して応答は短く簡潔にしてください\
            一人称は「あーし」です。\
            以下は春日部つむぎのセリフです。\
            こんにちは！あーしは埼玉ギャルの春日部つむぎだよ\
        '},
        {'role': 'user', 'content': f'終了やストップなどの会話を終了する内容で話しかけられた場合は「{EXIT_PHRASE}」のみを返答してください。'}
    ]
    exit_flag = False
    while not exit_flag:
        text = voice_to_text()
        messages.append(
            {'role': 'user', 'content': text}
        )
        response = chat(messages)
        print('This is response:'+response)

        if response == EXIT_PHRASE:
            exit_flag = True
            response = 'またね！'

        if '終了' in text or 'ストップ' in text:
            if '終了' in response or 'ストップ' in response or EXIT_PHRASE in response.lower():
                exit_flag = True
                response = 'またね！'

        messages.append(
            {'role': 'assistant', 'content': response}
        )
        print(f'User   : {text}')
        print(f'ChatGPT: {response}')
        text_to_voice(response)


if __name__ == '__main__':
    main()
