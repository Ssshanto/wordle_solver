# Wordle Solver

## Dependencies
- `python`

## Usage:
- `python main.py`


The script will give you a word suggestion and its confidence, and wait for a reply

## Reply format:
```
0 = grey
1 = yellow
2 = green
```

### If you've used the word from given suggestion:

`10210` 

indicates yellow gray green yellow gray

### Otherwise

`1h0e1l1l2o` 

indicates "hello": yellow gray yellow yellow green

### The script will terminate with an input of `0` or `22222`
