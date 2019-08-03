% Points on hexagon. Calculates the coorinates of where the numbers need to
% be.

function [M,N] = hexPoints(hexNumber)

% Number of points on the particular hexagon
if hexNumber == 0
    
    U = 0;
    V = 0;
    
          plott(U,V,hexNumber);
    %Center coordinates are an exception
    M = U;
    N = V;
    
else
    theta = 0 : pi/3 : 2*pi;
    theta = theta + pi/2;
    r = ones(1,7);
    
    %Cartesian coordinates of the vertices of the hexagon is
    %1x7 matrices
    [U,V] = pol2cart(theta,hexNumber*r);
    [M,N] = midpointss(U,V,hexNumber);
            plott(M,N,hexNumber);
    
end

end

