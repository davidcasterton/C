class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # out = {i: "" for i in range(math.ceil(words/maxWidth))}

        out = []  # final output list
        wr = []  # current words in row
        rlen = 0  # current row length

        for word in words:
            wlen = len(word)  # current word length

            # pack current words to row string, then create new row
            if rlen + wlen + len(wr) > maxWidth:
                sn = maxWidth - rlen  # spaces needed
                ns = len(wr) # number of remaining spaces between words

                # add words to row in reverse, with increasing spaces as go
                row = ""
                for i in range(len(wr)-1, -1, -1):
                    ws = math.floor(sn / ns) if ns>0 else 1  # spaces between words, rounded down
                    if i == len(wr)-1:
                        ws = 0  # if 1st word (right), no spaces
                    elif i == 0:
                        ws = sn  # if last word (left), use all remaining spaces
                    elif ws == 0:
                        ws = 1
                    row = wr[i] + " "*ws + row  # join into string
                    sn -= ws
                    ns -= 1
                    print(f'{i} {maxWidth=} {rlen=} {sn=} {ns=} {ws=} {row=}')

                row += " " * (maxWidth-len(row))  # right pad, if needed
                out.append(row)

                # reset running variables
                wr = []
                rlen = 0

            # add word to row
            wr.append(word)
            rlen += len(word)

        if wr:
            sn = maxWidth - (rlen + len(wr) - 1)  # spaces needed
            row = (" ").join(wr) + " "*sn  # join into string
            out.append(row)

        return out
