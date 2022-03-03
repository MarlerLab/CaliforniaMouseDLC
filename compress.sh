./ffmpeg -ss 00:00:10 -i $1 -vf scale=480:-2,setsar=1:1,fps=10 -c:v libx264 -c:a copy $2
