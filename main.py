"""
Wordcloud source code here:
https://github.com/amueller/word_cloud/tree/main

Wordcloud docs here:
https://amueller.github.io/word_cloud/

"""
from pandas import read_csv
from random import shuffle, randint
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def grey_color_func(
    word,
    font_size,
    position,
    orientation,
    random_state=None,
    **kwargs,
):
    #return f"hsl({randint(0, 100)}, {60}%, {randint(30, 80)}%)"
    return f"hsl(0, 0%, 100%)"

def make_wordcloud(text: str):
    """Create a wordcloud from the text file"""
    wc = WordCloud(
        width=1584,
        height=396,        
        prefer_horizontal=0.8,
        scale=1,
        max_font_size=100,
        min_font_size=4,
        background_color='dimgray',
        max_words=1000,
        colormap='Pastel2',#'Accent',
        random_state=1,
    ).generate(text)

    plt.figure()
    plt.imshow(
        #wc.recolor(color_func=grey_color_func),
        wc,
        interpolation="bilinear",
    )
    plt.axis("off")
    plt.savefig('wordcloud.png', dpi=1000, bbox_inches="tight", pad_inches=0.0)
    plt.show()  


def csv_to_string(filepath: str) -> str:
    """
    Convert a CSV table to a string ofr the wordcloud.
    The table should have two columns: 'word', 'weight'
    """
    df = read_csv(WORDS_FILEPATH).dropna()
    words = []
    for _, row in df.iterrows():
        words += [row["word"]] * int(row["weight"])
    shuffle(words)
    print(f"Using {len(df['word'].unique())} unique words")
    return ' '.join(words)


if __name__ == "__main__":
    

    WORDS_FILEPATH = "words.csv"
    text = csv_to_string(WORDS_FILEPATH)

    make_wordcloud(text)