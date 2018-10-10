__version__ = "1.0"

from meshroom.core import desc


class UndistortImages(desc.CommandLineNode):
    commandLine = 'aliceVision_undistortImages {allParams}'
    size = desc.DynamicNodeSize('input')
    parallelization = desc.Parallelization(blockSize=40)
    commandLineRange = '--rangeStart {rangeStart} --rangeSize {rangeBlockSize}'

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='''SfMData file.''',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='outputFileType',
            label='Output File Type',
            description='Output file type for the undistorted images.',
            value='exr',
            values=['jpg', 'png', 'tif', 'exr'],
            exclusive=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='saveMetadata',
            label='Save Metadata',
            description='Save projections and intrinsics informations in images metadata (only for .exr images).',
            value=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='saveMatricesTxtFiles',
            label='Save Matrices Text Files',
            description='Save projections and intrinsics informations in text files.',
            value=False,
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        ),
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output',
            description='''Output folder.''',
            value=desc.Node.internalFolder,
            uid=[],
        )
    ]
