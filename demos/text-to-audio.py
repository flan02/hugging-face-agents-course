from gtts import gTTS
import os

text = """ it was a morning when I
could find you

and your skin was kissed by a 
hot breeze of june

your eyes were pretty,
I adored their blue

and those nights when I
love you, ooh

so blue, and when in silence
I kissed your sweet lips

so blue, I had the feeling
of a growing love

so blue, I look skyward
and then I can see

that you are the star
of my dreams...





so blue, because this love is as blue
as the sky

so blue, how from your lovely first look
all my hope arose

as blue as crying when there is no
more bad blood

it's pure and it's so blue that it got
the heart drunk

because this love is as blue
as the sky

so blue, like the blue of a deep sea, it was
born for both

as blue as the blue giant that is
this mad lust

a spring which is so blue that fills me
with real love





you are the wonder that I
wanted for me

you are the girl that I
wanted to meet

so blue, I wish understand
your innocent being

I will be your fairy
tale prince...

so blue, so is my madness
if I am with you

so blue, you will be a moonbeam at night
for me too

so blue, and with the rain, fully
painted light blue

forever I will love
only you, ooh

so blue, because this love is as blue
as the sky

so blue, how from your lovely first look
all my hope arose

as blue as crying when there is no
more bad blood

it's pure and it's so blue that it got
the heart drunk

because this love is as blue
as the sky

so blue, like the blue of a deep sea, it was
born for both

as blue as the blue giant that is
this mad lust

a spring which is so blue that fills me
with real love

so blue, because this love is as blue
as the sky

so blue, how from your lovely first look
all my hope arose

as blue as crying when there is no
more bad blood

it's pure and it's so blue that it got
the heart drunk

because this love is as blue
as the sky

so blue, like the blue of a deep sea, it was
born for both

as blue as the blue giant that is
this mad lust

a spring which is so blue that fills me
with real love

because this love is as blue
as the sky

so blue, how from your lovely first look
all my hope arose

as blue as crying when there is no
more bad blood

it's pure and it's so blue that it got
the heart drunk

because this love is as blue
as the sky

so blue, like the blue of a deep sea, it was
born for both

as blue as the blue giant that is
this mad lust

a spring which is so blue that fills me
with real love

because this love is as blue
as the sky

so blue, how from your lovely first look
all my hope arose

as blue as crying when there is no
more bad blood

it's pure and it's so blue that it got
the heart drunk

because this love is as blue
as the sky

so blue, like the blue of a deep sea, it was
born for both

as blue as the blue giant that is
this mad lust

a spring which is so blue that fills me
with real love 
"""
tts = gTTS(text=text, lang='en')
tts.save("soblue-lyrics.mp3")

# Reproduce (en Windows):
os.system("start soblue-lyrics.mp3")

