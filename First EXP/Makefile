CC = gcc
CFLAGS = -Iinclude -Wall
SRC = src/First.c src/Second.c src/Third.c src/Fourth.c
OBJ = $(SRC:.c=.o)
TARGET = my_library

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)