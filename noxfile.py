# type: ignore
import nox


@nox.session
def python(session):
    session.install("pytest", "maturin")
    session.install(".", "--no-build-isolation")
    session.run("make", "test", external=True)
