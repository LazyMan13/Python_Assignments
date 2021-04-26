formatter = "{}{}{}{}{}"
slash = "\N{SOLIDUS}"
uValue = "\u0068\u0074\u0074\u0070\u0073\u003a"
xValue = "\x64\x51\x77\x34\x77\x39\x57\x67\x58\x63\x51"
main = "youtu.be"
site = formatter.format(uValue,slash*2,main,slash,xValue)

message = '''
Check out this cool Python tutorial I found:
{}
'''
print(message.format(site))
