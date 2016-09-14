%Make a terrain image of the test terrain. 500x500 px

%Create the terrain
x=linspace(0,10,500);
y=linspace(0,10,500);
terr=transpose(x)*y;
for i=1:length(x)
    for j=1:length(y)
        terr(i,j)=TerrainFunc(x(i),y(j));
    end
end
terr=uint8(terr/max(max(terr))*255);
imwrite(terr,'terrain_test2.jpg')