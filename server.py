from flask import Flask

app = Flask(__name__)

@app.route('/get_example/',methods=['GET'])
def get_example():
	return "some data\n"


@app.route('/switch_example/<int:switch_num>',methods=['POST'])
def switch_example(switch_num):
	print("change state of, switch #", switch_num)

	# output_example = "switch #"+ switch_num
	return "switch #" + str(switch_num) + " state changed\n"


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=int("8080"))


