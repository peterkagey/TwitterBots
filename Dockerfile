FROM public.ecr.aws/lambda/python:3.8

RUN pip install tweepy
RUN pip install Pillow -t .

COPY botfons_needles/needle_drawer.py ./botfons_needles/
COPY botfons_needles/random_needle.py ./botfons_needles/
COPY botfons_needles/secrets.py       ./botfons_needles/
COPY botfons_needles/tweet_builder.py ./botfons_needles/
COPY botfons_needles/tweeter.py       ./botfons_needles/

COPY botzier_curves/caption_maker.py   ./botzier_curves/
COPY botzier_curves/curve_drawer.py    ./botzier_curves/
COPY botzier_curves/secrets.py         ./botzier_curves/
COPY botzier_curves/tweeter.py         ./botzier_curves/

COPY oeis_triangles/b_file_lookup.py   ./oeis_triangles/
COPY oeis_triangles/b_file_parser.py   ./oeis_triangles/
COPY oeis_triangles/data.json          ./oeis_triangles/
COPY oeis_triangles/json_accountant.py ./oeis_triangles/
COPY oeis_triangles/oeis_drawer.py     ./oeis_triangles/
COPY oeis_triangles/secrets.py         ./oeis_triangles/
COPY oeis_triangles/sequence_drawer.py ./oeis_triangles/
COPY oeis_triangles/triangle_drawer.py ./oeis_triangles/
COPY oeis_triangles/tweeter.py         ./oeis_triangles/

COPY robot_walks/robot_walk_drawer.py  ./robot_walks/
COPY robot_walks/secrets.py            ./robot_walks/
COPY robot_walks/turn.py               ./robot_walks/
COPY robot_walks/tweeter.py            ./robot_walks/

COPY xor_triangles/rows2.json          ./xor_triangles/
COPY xor_triangles/rows3.json          ./xor_triangles/
COPY xor_triangles/secrets.py          ./xor_triangles/
COPY xor_triangles/seed_maker.py       ./xor_triangles/
COPY xor_triangles/triangle_drawer.py  ./xor_triangles/
COPY xor_triangles/triangle_grower.py  ./xor_triangles/
COPY xor_triangles/tweeter.py          ./xor_triangles/

COPY tweeter.py ./
COPY app.py     ./

CMD ["app.handler"]
