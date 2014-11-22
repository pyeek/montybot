# _*_ coding: utf-8 -*-
from ..puppy_plugin.get_puppy import PuppyFetch


class DescriptivePlugin(object):
    registered_descriptions = (
        'tasty',
        'lame',
        'funny',
        'amazing',
        )
        
    @classmethod
    def run(cls, user, channel, message, bot_instance, fetcher=PuppyFetch):
        """
        Descriptive plugin::

            'Some tasty sushi'
        """
        if user != bot_instance.nickname:
            return

        message_words = message.lower().split()
        punctuation_set = set(string.punctuation)
        for registered in cls.registered_descriptions:
            try:
                subject_word = message_words[message_words.index(registered.lower()) + 1]
                subject = ''.join(ch for ch in subject if ch not in punctuation_set)
            except IndexError:
                continue
                
            bot_instance.handled = True
            reply = fetcher.get(subject)
            bot_instance.msg(channel, reply)
        return reply


if __name__ == "__main__":
    from mock import Mock

    def mock_msg(chan, msg):
        print chan
        print msg
    
    bot_instance = Mock()
    bot_instance.msg = mock_msg

    reply = DescriptivePlugin.run('test', '#scoobydoo', "that's some tasty sushi", bot_instance)
    assert reply == 'sushi'
