% Plotting of points to better visualize
function plott(M,N,hexNumber)

% Plotting '*' everywhere the number is supposed to be

% plot(M,N,'*')

if hexNumber ==0
    % Labeling the center
    text(M,N,'1')
else
    % Labeling the points with corresponding numbers to verif
    label = 6*sum(0:(hexNumber-1))+2:6*sum(0:hexNumber)+1;
    for a = 1:length(M)
        text(M(a),N(a),num2str(label(a)));
    end
end

hold on;
axis equal

end
