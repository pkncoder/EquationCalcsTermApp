from math import sqrt
import click

@click.group()
def cli():
    pass

# This command takes point one and point two (givin by user)
# It prints the distance between them
@click.command(name="dist")
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
@click.command(name="mid")
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

# This will split a line on a givin ratio
@click.command(name="RatFind")
@click.argument("point1")
@click.argument("point2")
@click.argument("ratio")
def ratioPointSplit(point1, point2, ratio):

    # Split the points
    # Point one
    x1, y1 = splitPoint(point1)

    # Point two
    x2, y2 = splitPoint(point2)

    # Split the ratio too
    partOne, partTwo = splitRatio(ratio)

    # Declare k, the part over whole of the ratio
    k = partOne / (partOne + partTwo)

    # Get the answers
    # Answer X
    ansX = k * (x2 - x1) + x1

    # Answer Y
    ansY = k * (y2 - y1) + y1

    # Get the answer by using the ratio split equation
    print(f"Splitting Point: ({round(ansX, 2)}, {round(ansY, 2)})")

# Get the ratio from the endpoint
@click.command(name="EndRat")
@click.argument("point1")
@click.argument("point2")
@click.argument("ratio")
def endpointFromRatio(point1, point2, ratio):
    
    # Get the points from point1
    # Point 1
    x1, y1 = splitPoint(point1)

    # Point 2
    x2, y2 = splitPoint(point2)

    # Ratio parts
    partOne, partTwo = splitRatio(ratio)

    # Get the answers
    # Answer X
    ansX = ((x2 - x1) / partOne) * (partOne + partTwo)

    # Answer Y
    ansY = ((y2 - y1) / partOne) * (partOne + partTwo)

    # Print the answer
    print(f"Endpoint: ({round(ansX, 2)}, {round(ansY, 2)})")


# Pythag leg+leg
@click.command(name="PythLL")
@click.argument("leg1")
@click.argument("leg2")
def pythagLegLeg(leg1, leg2):

    # Get the answer using the pythag thearum (idk how to spel)
    ans = sqrt(float(leg1)**2 + float(leg2)**2)

    # Print the answer
    print(f"Hype Length: {round(ans, 2)}")


# Pythag leg+hype
@click.command(name="PythHL")
@click.argument("hype")
@click.argument("leg")
def pythagHypeLeg(hype, leg):

    # Get the ans using the re-arranged pythag alg to get a leg
    ans = sqrt(float(hype)**2 - float(leg)**2)

    # Print the answer
    print(f"Other Leg Length: {round(ans, 2)}")


# Add the commands
cli.add_command(distance)
cli.add_command(midpoint)
cli.add_command(ratioPointSplit)
cli.add_command(endpointFromRatio)
cli.add_command(pythagLegLeg)
cli.add_command(pythagHypeLeg)


# Split a point into x1 and y1
def splitPoint(point):

    # Split the point
    x1 = float(point.split(",")[0])
    y1 = float(point.split(",")[1])

    # Return x1 and y1
    return x1, y1

# This will return the two parts of a ratio
def splitRatio(ratio):

    # Split the ratio along the colon
    # Part one of the ratio
    partOne = float(ratio.split(":")[0])

    # Part two of the ratio
    partTwo = float(ratio.split(":")[1])

    # Return the part one and two
    return partOne, partTwo


if __name__ == "__main__":
    cli()