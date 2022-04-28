import os


def load_config():
    _, d, _ = next(os.walk('./'))
    d = [_ for _ in d if _.startswith("californiamouse-marlerlab")]
    assert len(d) == 1, "There must be only one project."
    return str(os.path.abspath(os.path.join(d[0], "config.yaml")))

