deploy:
	sam validate
	sam deploy

invoke:
	sam local invoke -e events/event.json SumAppFunction

test:
	pytest
