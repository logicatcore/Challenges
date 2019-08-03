% Since after the first hexagon the numbers start occupying the positions
% along the edges of the Hexagon in a incrimental fashion. That observation
% is used to find the coordinates of the numbers and position them
% accordingly.

function [M,N] = midpointss(X,Y,hexNumber)

iteration = 0;
i = 1;
M = zeros(1,6*hexNumber);
N = zeros(1,6*hexNumber);

while i <= 6*hexNumber
    % Number of mid points based on the hexagon number
    midPoints = hexNumber-1;
    % This is used to keep track of calculation occuring on which line
    iteration = iteration + 1;
    M(i) = X(iteration);
    N(i) = Y(iteration);
    
    if midPoints ~= 0
        % m+n the ratio is same for all divisions
        denominator = midPoints + 1;
        j=1;
        
        while midPoints>0
            i = i + 1;
            
            M(i) = (j*X(iteration+1)+midPoints*X(iteration))/denominator;
            N(i) = (j*Y(iteration+1)+midPoints*Y(iteration))/denominator;
            
            midPoints = midPoints - 1;
            j = j+1;
        end
    end
    i = i+1;
end
end
