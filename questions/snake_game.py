#define WIDTH 100
#define HEIGHT 100
#define LENGTH 10

import random
import enum


volatile bool screen[WIDTH][HEIGHT];
volatile bool *up;
volatile bool *down;
volatile bool *right;
volatile bool *left;

// Put state here.
directions = enum.Enum():
  up = 'UP'
  down = 'DOWN'
  right = 'RIGHT'
  left = 'LEFT'
current_direction = None


class Point(object):
  def __init__(x, y):
    self.x = x
    self.y = y

points = []   // list of points

void end_of_game();

void init() {
  x = random.randint(LENGTH, WIDTH-LENGTH)
  y = random.randint(LENGTH, HEIGHT-LENGTH)
  points.append(Point(x, y))  // index 0 head of snake
  for i in range(LENGTH - 1):
    x -= 1
    points.append(Point(x, y))
  current_direction = directions.right.value

  // TODO init screen
}

void cycle() {
  // Get the user input
  if (*up) {
    current_direction = directions.up.value
  } else if (*down) {
    current_direction = directions.down.value
  } else if (*right) {
    current_direction = directions.right.value
  } else if (*left) {
    current_direction = directions.left.value
  }

  // Move the snake by 1 pixel
  if (current_direction == directions.up.value) {
    new_x = points[0].x
    new_y = points[0].y + 1
  } else if (current_direction == directions.down.value) {
    new_x = points[0].x
    new_y = points[0].y - 1
  } else if (current_direction == directions.right.value) {
    new_x = points[0].x + 1
    new_y = points[0].y
  } else if (current_direction == directions.left.value) {
    new_x = points[0].x - 1
    new_y = points[0].y
  } else {
    // error handling, should never reach here
  }
  point_to_remove = points[-1]
  point_to_insert = Point(new_x, new_y)

  // update points list
  points.pop(LENGTH-1)  // remove tail of snake
  point.insert(0, point_to_insert)  // insert new head of snake

  // Update the screen
  screen[point_to_remove.x][point_to_remove.y] = False  // remove old tail
  screen[point_to_insert.x][point_to_insert.y] = True  // insert new head

  // Check for end-of-game
  // check if head hits screen edge
  if (point_to_insert.x < 0 || point_to_insert.x > WIDTH):
    end_of_game()
  else if (point_to_insert.y < 0 || point_to_insert.y > HEIGHT):
    end_of_game()
  // check if head hits body
  for point in points[1:]:
    if (point_to_insert.x == point.x) and (point_to_insert.y == point.y):
      end_of_game()

}
