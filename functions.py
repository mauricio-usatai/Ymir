# Your code goes here
def challenge_1(_input):
    return True

def challenge_2(_input):
    import pandas as pd
    d1, d2 = _input
    df1 = pd.DataFrame(d1)
    df2 = pd.DataFrame(d2)

    df = df1.append(df2)
    df = df.reset_index()

    df = df.rename(columns={'A': 'Gender', 'B': 'Age'})

    return int(df[df['Gender'] == 'female']['Gender'].count())

def challenge_3(_input):
    return True

