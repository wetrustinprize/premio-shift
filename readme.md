Premio's Shift is a very simple text encryption, you can use it to send _secret messages_ to your friends.

## Table of Content

- [Table of Content](#table-of-content)
- [How it works](#how-it-works)
- [How to use](#how-to-use)
  - [CLI Interface](#cli-interface)
    - [Simple shift](#simple-shift)
    - [Decrypt a message](#decrypt-a-message)
    - [Using From and To](#using-from-and-to)

## How it works

- A **Shift** is a message encrypted using Premio's Shift.
- Every Shift has a **key** to encrypt and decrypt
- The key has no **char limit**
- A key only has **alphabetic characters** and **numbers**, everything else is ignored
- Messages have a **position**, being **0 the initial state**

---

Lets look at this example using the message "ahz159" and key "2ca".

| Position | Message |
| -------- | ------- |
| 0        | ahz159  |
| 1        | cja380  |
| 25       | ydy104  |

1. First, the key is converted to a list of key numbers, in this case: [2, 3, 1]
   - 2 is a **number**, so we **keep it**;
   - "c" is a **letter**, so we get it's **position in the alphabet**, in this case: 3
   - "a" is a **letter**, so we get it's **position in the alphabet**, in this case: 1
1. Now multiply the list by the amount if shift we want in the message
   - If the shift is 25, we multiply all the numbers inside the key numbers list, like so:
   - `[2, 3, 1] * 25 = [50, 75, 25]`
1. For each letter in the message take the corresponding number in the key numbers list and then get the new letter by summing the current place in alphabet plus the corresponding number in the key number list
   - If there is no more key number list, we start over from the first number in the list

---

## How to use

### CLI Interface

You can encrypt or decrypt yout message only using your terminal.

```shell
$ python3 cli.py -h
usage: cli.py [-h] [-m MESSAGE] [-k KEY] [-s SHIFT] [-p POS] [-t TO]
```

| Argument | Flag           | Description                                                                                                   |
| -------- | -------------- | ------------------------------------------------------------------------------------------------------------- |
| Message  | -m / --message | The message to shift                                                                                          |
| Key      | -k / --key     | The key to use in the shifting process                                                                        |
| Shift    | -s / --shift   | **optional**, the total steps to shift                                                                        |
| Pos      | -p / --pos     | **optional**, the initial position of the message                                                             |
| To       | -t / --to      | **optional**, will move the correct amount of steps to move the message to this position. (requires -p value) |

---

#### Simple shift

A simple shift, encrypting the message "Hello world" with the key 123.

```shell
$ python3 cli.py -m "Hello world" -k 123 -s 25
Gcikm vmokb
```

---

#### Decrypt a message

Using the result from the example above, its possible decrypt the message knowing the current position the message is.

```shell
$ python3 cli.py -m "Gcikm vmokb" -k 123 -s -25
Hello world
```

It is also posible to use the From and To arguments to decrypt a message.

```shell
$ python3 cli.py -m "Gcikm vmokb" -k 123 -p 25 -t 0
Hello world
```

---

#### Using From and To

In this example the message is decrypted and then is shifted +1.

```shell
$ python3 cli.py -m "Gcikm vmokb" -k 123 -p 25 -t 0 -s 1
Igomq xqumf
```
