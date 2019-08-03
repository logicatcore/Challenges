%Draw Hexagon i.e., to draw the boudaries of each number
function [minX,maxX,minY,maxY] = drawHexagon(Xcoord,Ycoord)
theta = 0 : pi/3: 2*pi;
theta = theta + pi/2;
r = ones(1,7);

[X,Y] = pol2cart(theta,r);

X = X + Xcoord;
Y = Y + Ycoord;

minX = min(X);
maxX = max(X);

minY = min(Y);
maxY = max(Y);

theta = 0 : pi/3: 2*pi;
[X,Y] = pol2cart(theta,0.56*r);
X = X + Xcoord;
Y = Y + Ycoord;
[theta,r] = cart2pol(X,Y);

    polar(theta,r);
end