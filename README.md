# Tic Tac Toe

This project consists of two major parts, a library called "t3" for representing
the rules of tic tac toe, and an untested prototype of a game runner that uses
the venerable "curses" library for graphics and the espeak binary for sound.

The t3.ai package contains an unoptimized implementation of the Minimax 
algorithm that performs very badly on nearly empty boards, but performs well
enough for a human player after the first two moves have been made. To cover
over the long delay, the game runner will use espeak in a subprocess to speak
with a synthesized voice while the player waits.

t3 represents my best effort in putting together a tic tac toe engine, although
there are still things I don't like about it (mainly awkward state validation
and a number of untested methods added to presenters late in development)

The curses prototype could use a lot of refactoring - there are a few modules
whose methods all take the same two or three parameters, when they could be
taking self instead. There are also substantial parts of it that you could 
easily put into a test harness.

## Changing Settings

You can change player names and symbols by editing settings.json in this
directory. Curses can behave oddly when exposed to full-width characters and
absolutely refuses to deal with characters from right-to-left languages.

## Installation

### Ubuntu

Provided you've installed ansible, run:

```
sudo ./bin/install
```

Or with much less ceremony:

```
sudo apt-get install espeak
sudo pip install subprocess32
```

### OSX

I haven't tested this install script on OSX yet, but you can try:

```
sudo ./bin/install-osx-dependencies.sh
```

which only contains the lines:

```
brew install espeak
pip install subprocess32
```

## Running Tests

A script "vagrant-watch" is provided in ./bin, that will bring up a known good
development environment by calling out to (Vagrant)[https://vagrantup.com] and
then use it to re-run the test suite every two seconds.

```
./bin/vagrant-watch
```

You can run tests on your local machine by running

```
make test
```

## Running

Maximize your terminal window (or make it at least 30x30) and run ./play
(assuming that 'python' on your system refers to 2.7)

Note that this game requires a terminal with colors and mouse support - on OSX,
you should try iTerm.

```
./play.py
```

## Known Issues

- The application crashes when you resize your terminal. This is of course
  avoidable, but I don't want to do any more forward development on the curses
  prototype without tests.
- You cannot run the curses prototype in the dev VM, because it has no sound
  devices configured.
- If the espeak binary is not present, the game will carry on with no sound.
  This is arguably not a problem, but it makes me a little uncomfortable to
  play fast and loose with subprocesses like this.
