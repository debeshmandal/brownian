from pathlib import Path

from hydrogels.trajectory.core import (
    ParticleFrame,
    ParticleTrajectory,
    TopologyFrame,
    TopologyTrajectory
)

FOLDER = Path(__file__).parent
H5 = FOLDER / '_test.h5'

def test_ParticleFrame():
    traj = ParticleTrajectory(H5)
    frame = traj.frames[0]
    frame.array
    frame.dataframe
    output = FOLDER / 'lammps.test.conf'
    frame.to_LAMMPS_dump(output)
    output.unlink()
    return

def test_ParticleTrajectory():
    traj = ParticleTrajectory(H5)
    traj.time
    traj.frames
    traj.box
    return

def test_TopologyFrame():
    traj = TopologyTrajectory(H5)
    frame = traj.frames[0]
    frame.dataframe

def test_TopologyTrajectory():
    traj = TopologyTrajectory(H5)
    traj.time
    traj.frames

if __name__ == '__main__':
    test_ParticleFrame()
    test_ParticleTrajectory()
    test_TopologyFrame()
    test_TopologyTrajectory()