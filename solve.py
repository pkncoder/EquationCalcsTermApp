from math import sqrt
import click

@click.group()
def cli():
    pass

# This command takes point one and point two (givin by user)
# It prints the distance between them
@click.command()
@click.argument("p1")
@click.argument("p2")
def distance(p1, p2):

    # X one and Y one get split from p1
    x1, y1 = splitPoint(p1)

    # X two and Y two get split from p2
    x2, y2 = splitPoint(p2)
    
    # Get the answer with the distance equation with the split points
    ans = sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Print the answer (rounded two 2 decimals)
    print(f"Distance: {round(ans, 2)}")

# Get the midpoint from point one and point two (givin by user)
@click.command()
@click.argument("p1")
@click.argument("p2")
def midpoint(p1, p2):
    # X one and Y one get split from p1
    x1, y1 = splitPoint(p1)

    # X two and Y two get split from p2
    x2, y2 = splitPoint(p2)
    
    # Get the answer with the midpoint equation with the split points
    # X portion
    ansX = ((x1 + x2) / 2)

    # Y portion
    ansY = ((y1 + y2) / 2)

    # Print the answer(s) (rounded two 2 decimals)
    print(f"Midpoint: ({round(ansX, 2)}, {round(ansY, 2)})")

# Add the commands
cli.add_command(distance)
cli.add_command(midpoint)


# Split a point into x1 and y1
def splitPoint(point):

    # Split the point
    x1 = float(point.split(",")[0])
    y1 = float(point.split(",")[1])

    # Return x1 and y1
    return x1, y1



if __name__ == "__main__":
    cli()
