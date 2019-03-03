numbers = load('numbers.txt');

max = 0;
%% horizontal
for i=1:20
    for j=1:17
       prod = 1;
       for k=0:3
          prod = prod * numbers(i,j+k); 
       end
       if(prod>max)
           max = prod;
       end
    end
end

%% vertical
for i=1:17
    for j=1:20
       prod = 1;
       for k=0:3
          prod = prod * numbers(i+k,j); 
       end
       if(prod>max)
           max = prod;
       end
    end
end

%% diagonal(left-right)
for i=1:17
    for j=1:17
       prod = 1;
       for k=0:3
          prod = prod * numbers(i+k,j+k); 
       end
       if(prod>max)
           max = prod;
       end
    end
end
%% diagonal(right-left)
for i=1:17
    for j=20:-1:4
       prod = 1;
       for k=0:3
          prod = prod * numbers(i+k,j-k); 
       end
       if(prod>max)
           max = prod;
       end
    end
end
max