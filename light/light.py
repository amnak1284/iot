from flask import Flask, render_template, request
import mraa
import time

lightapp = Flask(__name__)
light = mraa.Gpio(2)
light.dir(mraa.DIR_OUT)

shortTime = .5
longTime = shortTime * 2

def blinkSequence(light, rest, numTimes):
	for _ in range(numTimes):
		light.write(1)
		time.sleep(rest)
		light.write(0)
		time.sleep(rest)

@lightapp.route("/", methods=["GET", "POST"])
def lightIO():
    if request.method == 'POST':

        blinkSequence(light, shortTime, 3)
        blinkSequence(light, longTime, 3)
        blinkSequence(light, shortTime, 3)
    return render_template('button.html')

if __name__ == '__main__':
	lightapp.run(host='0.0.0.0')




