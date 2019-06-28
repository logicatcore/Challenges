%Main program:
% -> Order of Operations
%
% -> Reproduce the hexagonal arrangement of numbers as per the problem-
%    -statement
%
% -> Identify the 6 neighbhouring numbers of all the numbers based on the-
%    -logic of nearest 6 numbers
%
% -> check if the center number is infact a factor of the product of the-
%    -6 neighbhouring numbers
%     1) Find the prime factors of the center number and the surronding
%     numbers
%     2) If all the prime factors of the center are present in the prime
%     factors of all the 6 neighbhouring numbers. Then the center number is a
%     factor of the 6 other numbers.
%
% stop the program when the 2000th number is found

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function  main(hexes)
tic
clc
% clear all
close all

% Number of concentric number of hexagons that the program has to run for
hexNumber = hexes;%400; %

% Variables to store the coordinates of the numbers in the hexagon arrangement
mainX = zeros(1,6*sum(1:hexNumber)+1);
mainY = zeros(1,6*sum(1:hexNumber)+1);

% Calculating the actual coordinates and plotting them if necessary to-
% -visualize

for i=0:hexNumber
    i;
    [coordX,coordY] = hexPoints(i);
    if i==0
        mainX(1) = coordX;
        mainY(1) = coordY;
    else
        mainX(1:6*sum(1:i)+1) = [mainX(1:6*sum(0:i-1)+1),coordX];
        mainY(1:6*sum(1:i)+1) = [mainY(1:6*sum(0:i-1)+1),coordY];
    end
end

% Storing the neighbhours i.e., the 6 numbers surronding every number-
% -in factors

factors = zeros(6*sum(0:hexNumber-1)+1,6);

% Since the last hexagon will not be having six surrounding neighbhours-
% we stop finding the neighbhours just a hexagon before the last one.
for i=1:6*sum(0:hexNumber-1)+1
    probe = i;
    [minX,maxX,minY,maxY] = drawHexagon(mainX(probe),mainY(probe));
    a = find(mainX>=minX-0.1 & mainX<=maxX+0.1);
    b = find(mainY(a)>=minY-0.1 & mainY(a)<=maxY+0.1);
    c = a(b);
    c(c == probe) = [];
    factors(i,:) = c';
end

% Solution function checks if the centre divides the product of the rest of
% the numbers exactly or not and keeps a count of how many satisfy the
% criteria.

[count,eureka] = solution(factors,hexNumber);
toc
end
