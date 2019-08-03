function [count,satisfy] = solution(factors,hexNumber)
count =1;
satisfy = zeros(1,2000);
satisfy(1,1) = 1;
%     for i=1:6*sum(0:hexNumber-1)+1

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% A crude way of checking if the centre is a factor of the product of the
% rest of the 6 numbers. Results were not conclusive hence tryed different
% approaches
%
%              if mod(prod(factors(i,:)),i) == 0

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%2nd method where in  a*b*c mod x = (a mod X) *(b mod X) * (c mod X)) mod X
%
%              if mod(mod(factors(i,1),i)*mod(factors(i,2),i)*mod(factors(i,3),i)...
%                 *mod(factors(i,4),i)*mod(factors(i,5),i)*mod(factors(i,6),i),i) == 0
%
%             count =count+1
%             satisfy(1,count) = i;
%             if count == 2000
%                 disp(i)
%                 break
%             end
%         end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3rd Method: The method that worked, find the prume factors and checks is
% all of the prime factors of center are present in the prime factors of
% rest of the surrounding numbers.

for i=2:6*sum(0:hexNumber-1)+1
    primefactors = [factor(factors(i,1)),factor(factors(i,2))...
        ,factor(factors(i,3)),factor(factors(i,4)),factor(factors(i,5))...
        ,factor(factors(i,6))];
    dividend = factor(i);
    for eks=1:length(dividend)
        if ismember(dividend(eks),primefactors) && length(dividend)==nnz(dividend)
            for irpselon=1:length(primefactors)
                if dividend(eks) == primefactors(irpselon)
                    primefactors(irpselon) = 0;
                    dividend(eks) = 1;
                    break
                end
            end
        else
            dividend(eks)=0;
            break
        end
    end
    
    if length(dividend)==nnz(dividend)
        count = count+1;
        satisfy(1,count) = i;
        if count == 2000 || count ==30
            disp(i)
            if count == 2000
                break
            end
        end
    end
end
end

