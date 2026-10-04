class MarvinMorseCoder:
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    @staticmethod
    def encode(text: str) -> str:
        line = [[t for t in t.upper()] for t in text.split()]
        line_lis = []
        morse = MarvinMorseCoder.MORSE_CODE
        n = ''
        for t in line:
            for i in t:
                for k, v in morse.items():
                    if i == k:
                        n += v + ' '
                        break
            line_lis.append(n)
            n = ''
        line_lis = [x[:-1] for x in line_lis]
        return '   '.join(line_lis)

    @staticmethod
    def decode(morse: str) -> str:
        line = []
        morse_dic = MarvinMorseCoder.MORSE_CODE
        text = [x.split() for x in morse.split('  ')]
        n = ''
        for t in text:
            for i in t:
                if i not in morse_dic.values():
                    n += '?'

                for k, v in morse_dic.items():
                    if i == v:
                        n += k
                        break
                    
            line.append(n)
            n = ''

        return ' '.join(line)


print(MarvinMorseCoder.encode("   hello   world   "))
print(MarvinMorseCoder.decode("..-. --- ---   -... .- .-."))