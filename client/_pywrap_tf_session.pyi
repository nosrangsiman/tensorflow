# Copyright 2023 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from typing import Any, ClassVar, Iterator, Optional

from typing import overload
TF_ABORTED: TF_Code
TF_BFLOAT16: TF_DataType
TF_BOOL: TF_DataType
TF_CANCELLED: TF_Code
TF_COMPLEX: TF_DataType
TF_COMPLEX128: TF_DataType
TF_COMPLEX64: TF_DataType
TF_DATA_LOSS: TF_Code
TF_DEADLINE_EXCEEDED: TF_Code
TF_DOUBLE: TF_DataType
TF_FAILED_PRECONDITION: TF_Code
TF_FLOAT: TF_DataType
TF_HALF: TF_DataType
TF_INT16: TF_DataType
TF_INT32: TF_DataType
TF_INT64: TF_DataType
TF_INT8: TF_DataType
TF_INTERNAL: TF_Code
TF_INVALID_ARGUMENT: TF_Code
TF_OK: TF_Code
TF_OUT_OF_RANGE: TF_Code
TF_PERMISSION_DENIED: TF_Code
TF_QINT16: TF_DataType
TF_QINT32: TF_DataType
TF_QINT8: TF_DataType
TF_QUINT16: TF_DataType
TF_QUINT8: TF_DataType
TF_RESOURCE: TF_DataType
TF_RESOURCE_EXHAUSTED: TF_Code
TF_STRING: TF_DataType
TF_UINT16: TF_DataType
TF_UINT32: TF_DataType
TF_UINT64: TF_DataType
TF_UINT8: TF_DataType
TF_UNAUTHENTICATED: TF_Code
TF_UNIMPLEMENTED: TF_Code
TF_UNKNOWN: TF_Code
TF_VARIANT: TF_DataType

class ItemsView:
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class KeysView:
    def __init__(self, *args, **kwargs) -> None: ...
    def __contains__(self, arg0: object) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class OpsById:
    def __init__(self) -> None: ...
    def items(self) -> ItemsView: ...
    def keys(self) -> KeysView: ...
    def values(self) -> ValuesView: ...
    def __bool__(self) -> bool: ...
    @overload
    def __contains__(self, arg0: int) -> bool: ...
    @overload
    def __contains__(self, arg0: object) -> bool: ...
    def __delitem__(self, arg0: int) -> None: ...
    def __getitem__(self, arg0: int) -> object: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: int, arg1: object) -> None: ...

class OpsByName:
    def __init__(self) -> None: ...
    def items(self) -> ItemsView: ...
    def keys(self) -> KeysView: ...
    def values(self) -> ValuesView: ...
    def __bool__(self) -> bool: ...
    @overload
    def __contains__(self, arg0: str) -> bool: ...
    @overload
    def __contains__(self, arg0: object) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> object: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: object) -> None: ...

class PyGraph:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def Dismantle(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _add_op(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _get_operation_by_name(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _op_def_for_type(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def get_operations(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def new_operations(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def num_operations(cls, *args, **kwargs) -> Any: ...
    @property
    def _nodes_by_id(self) -> OpsById: ...
    @property
    def _nodes_by_name(self) -> OpsByName: ...
    @property
    def _version_def(self) -> bytes: ...
    @property
    def operations(self) -> list: ...
    @property
    def version(self) -> int: ...

class PyOperation:
    graph: object
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def _add_control_input(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _add_control_inputs(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _add_outputs(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _init_outputs(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _remove_all_control_inputs(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _set_device_from_string(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _tf_input(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _tf_output(cls, *args, **kwargs) -> Any: ...
    @property
    def _c_op(self) -> TF_Operation: ...
    @property
    def _control_outputs(self) -> list: ...
    @property
    def _is_stateful(self) -> bool: ...
    @property
    def _node_def(self) -> bytes: ...
    @property
    def _op_def(self) -> bytes: ...
    @property
    def control_inputs(self) -> list: ...
    @property
    def device(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def outputs(self) -> list: ...
    @property
    def type(self) -> str: ...

class PyTensor:
    _id: object
    _name: object
    _shape_val: object
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def _as_tf_output(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _rank(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def _set_shape(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def consumers(cls, *args, **kwargs) -> Any: ...
    @property
    def _dtype(self) -> object: ...
    @property
    def _op(self) -> object: ...
    @property
    def _shape(self) -> object: ...
    @property
    def device(self) -> str: ...
    @property
    def graph(self) -> object: ...
    @property
    def ndim(self) -> int: ...
    @property
    def op(self) -> object: ...
    @property
    def value_index(self) -> int: ...

class TF_ApiDefMap:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Buffer:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Code:
    __members__: ClassVar[dict] = ...  # read-only
    TF_ABORTED: ClassVar[TF_Code] = ...
    TF_CANCELLED: ClassVar[TF_Code] = ...
    TF_DATA_LOSS: ClassVar[TF_Code] = ...
    TF_DEADLINE_EXCEEDED: ClassVar[TF_Code] = ...
    TF_FAILED_PRECONDITION: ClassVar[TF_Code] = ...
    TF_INTERNAL: ClassVar[TF_Code] = ...
    TF_INVALID_ARGUMENT: ClassVar[TF_Code] = ...
    TF_OK: ClassVar[TF_Code] = ...
    TF_OUT_OF_RANGE: ClassVar[TF_Code] = ...
    TF_PERMISSION_DENIED: ClassVar[TF_Code] = ...
    TF_RESOURCE_EXHAUSTED: ClassVar[TF_Code] = ...
    TF_UNAUTHENTICATED: ClassVar[TF_Code] = ...
    TF_UNIMPLEMENTED: ClassVar[TF_Code] = ...
    TF_UNKNOWN: ClassVar[TF_Code] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TF_DataType:
    __members__: ClassVar[dict] = ...  # read-only
    TF_BFLOAT16: ClassVar[TF_DataType] = ...
    TF_BOOL: ClassVar[TF_DataType] = ...
    TF_COMPLEX: ClassVar[TF_DataType] = ...
    TF_COMPLEX128: ClassVar[TF_DataType] = ...
    TF_COMPLEX64: ClassVar[TF_DataType] = ...
    TF_DOUBLE: ClassVar[TF_DataType] = ...
    TF_FLOAT: ClassVar[TF_DataType] = ...
    TF_HALF: ClassVar[TF_DataType] = ...
    TF_INT16: ClassVar[TF_DataType] = ...
    TF_INT32: ClassVar[TF_DataType] = ...
    TF_INT64: ClassVar[TF_DataType] = ...
    TF_INT8: ClassVar[TF_DataType] = ...
    TF_QINT16: ClassVar[TF_DataType] = ...
    TF_QINT32: ClassVar[TF_DataType] = ...
    TF_QINT8: ClassVar[TF_DataType] = ...
    TF_QUINT16: ClassVar[TF_DataType] = ...
    TF_QUINT8: ClassVar[TF_DataType] = ...
    TF_RESOURCE: ClassVar[TF_DataType] = ...
    TF_STRING: ClassVar[TF_DataType] = ...
    TF_UINT16: ClassVar[TF_DataType] = ...
    TF_UINT32: ClassVar[TF_DataType] = ...
    TF_UINT64: ClassVar[TF_DataType] = ...
    TF_UINT8: ClassVar[TF_DataType] = ...
    TF_VARIANT: ClassVar[TF_DataType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TF_DeprecatedSession:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_ImportGraphDefOptions:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_ImportGraphDefResults:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Input:
    index: int
    oper: TF_Operation
    def __init__(self) -> None: ...

class TF_Library:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Operation:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_OperationDescription:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Output:
    index: int
    oper: TF_Operation
    def __init__(self) -> None: ...

class TF_Server:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Session:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_SessionOptions:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Status:
    def __init__(self, *args, **kwargs) -> None: ...

class ValuesView:
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

def AddWhileInputHack(arg0: PyGraph, arg1: TF_Output, arg2: TF_Operation) -> None: ...
def ClearAttr(arg0: PyGraph, arg1: TF_Operation, arg2: str) -> None: ...
@overload
def EqualAttrValueWrapper(arg0: str, arg1: str) -> str: ...
@overload
def EqualAttrValueWrapper(arg0: str, arg1: str) -> str: ...
def EqualGraphDefWrapper(arg0: str, arg1: str) -> str: ...
def ExtendSession(arg0: TF_Session) -> None: ...
def GetHandleShapeAndType(arg0: PyGraph, arg1: TF_Output) -> bytes: ...
def GetOperationInputs(arg0: TF_Operation) -> list[TF_Output]: ...
def SetAttr(arg0: PyGraph, arg1: TF_Operation, arg2: str, arg3: TF_Buffer) -> None: ...
def SetFullType(arg0: PyGraph, arg1: TF_Operation, arg2: TF_Buffer) -> None: ...
def SetHandleShapeAndType(arg0: PyGraph, arg1: TF_Output, arg2: bytes) -> None: ...
def TF_AddControlInput(arg0: TF_OperationDescription, arg1: TF_Operation) -> None: ...
def TF_AddInput(arg0: TF_OperationDescription, arg1: TF_Output) -> None: ...
def TF_AddInputList(arg0: TF_OperationDescription, arg1: object) -> None: ...
def TF_ApiDefMapGet(arg0: TF_ApiDefMap, arg1: str, arg2: int) -> TF_Buffer: ...
def TF_ApiDefMapPut(arg0: TF_ApiDefMap, arg1: str, arg2: int) -> None: ...
def TF_CloseSession(arg0: TF_Session) -> None: ...
def TF_CreatePlaceholders(arg0: PyGraph, arg1: object, arg2: str) -> list[TF_Output]: ...
def TF_DeleteApiDefMap(arg0: TF_ApiDefMap) -> None: ...
def TF_DeleteBuffer(arg0: TF_Buffer) -> None: ...
@overload
def TF_DeleteDeviceList(arg0: TF_DeviceList) -> None: ...
@overload
def TF_DeleteDeviceList(arg0: TF_DeviceList) -> None: ...
def TF_DeleteFunction(arg0: TF_Function) -> None: ...
def TF_DeleteImportGraphDefOptions(arg0: TF_ImportGraphDefOptions) -> None: ...
def TF_DeleteImportGraphDefResults(arg0: TF_ImportGraphDefResults) -> None: ...
def TF_DeleteLibraryHandle(arg0: TF_Library) -> None: ...
def TF_DeleteSession(arg0: TF_Session) -> None: ...
def TF_DeleteSessionOptions(arg0: TF_SessionOptions) -> None: ...
def TF_DeleteStatus(arg0: TF_Status) -> None: ...
def TF_DeviceListCount(arg0: TF_DeviceList) -> int: ...
def TF_DeviceListIncarnation(arg0: TF_DeviceList, arg1: int) -> int: ...
def TF_DeviceListMemoryBytes(arg0: TF_DeviceList, arg1: int) -> int: ...
def TF_DeviceListName(arg0: TF_DeviceList, arg1: int) -> str: ...
def TF_DeviceListType(arg0: TF_DeviceList, arg1: int) -> str: ...
def TF_FinishOperation(arg0: TF_OperationDescription) -> TF_Operation: ...
def TF_FunctionImportFunctionDef(arg0: bytes) -> TF_Function: ...
def TF_FunctionImportFunctionDefNoSerialization(arg0) -> TF_Function: ...
def TF_FunctionSetAttrValueProto(arg0: TF_Function, arg1: str, arg2: bytes) -> None: ...
def TF_FunctionToFunctionDef(arg0: TF_Function, arg1: TF_Buffer) -> None: ...
def TF_GetAllOpList() -> TF_Buffer: ...
def TF_GetAllRegisteredKernels() -> TF_Buffer: ...
def TF_GetBuffer(arg0: TF_Buffer) -> object: ...
def TF_GetCode(arg0: TF_Status) -> TSL_Code: ...
def TF_GetOpList(arg0: TF_Library) -> object: ...
def TF_GetRegisteredKernelsForOp(arg0: str) -> TF_Buffer: ...
def TF_GetXlaAutoJitEnabled() -> int: ...
def TF_GetXlaConstantFoldingDisabled() -> int: ...
def TF_GraphCopyFunction(arg0: PyGraph, arg1: TF_Function, arg2: TF_Function) -> None: ...
def TF_GraphImportGraphDefWithResults(arg0: PyGraph, arg1: TF_Buffer, arg2: TF_ImportGraphDefOptions) -> TF_ImportGraphDefResults: ...
def TF_GraphImportGraphDefWithResultsNoSerialization(arg0: PyGraph, arg1, arg2: TF_ImportGraphDefOptions) -> TF_ImportGraphDefResults: ...
def TF_GraphNextOperation(arg0: PyGraph, arg1: int) -> tuple: ...
def TF_GraphRemoveFunction(arg0: PyGraph, arg1: str) -> None: ...
def TF_GraphSetOutputHandleShapesAndTypes_wrapper(arg0: PyGraph, arg1: TF_Output, arg2: list[Optional[list[int]]], arg3: list[int], arg4: object) -> None: ...
def TF_GraphToFunction_wrapper(arg0: PyGraph, arg1: str, arg2: bool, arg3: Optional[list[TF_Operation]], arg4: list[TF_Output], arg5: list[TF_Output], arg6: list[bytes], arg7: list[TF_Operation], arg8: list[bytes], arg9: None, arg10: str) -> TF_Function: ...
def TF_GraphToGraphDef(arg0: PyGraph, arg1: TF_Buffer) -> None: ...
def TF_GraphToGraphDefPybind(*args, **kwargs) -> Any: ...
def TF_ImportGraphDefOptionsAddInputMapping(arg0: TF_ImportGraphDefOptions, arg1: str, arg2: int, arg3: TF_Output) -> None: ...
def TF_ImportGraphDefOptionsAddReturnOperation(arg0: TF_ImportGraphDefOptions, arg1: str) -> None: ...
def TF_ImportGraphDefOptionsAddReturnOutput(arg0: TF_ImportGraphDefOptions, arg1: str, arg2: int) -> None: ...
def TF_ImportGraphDefOptionsRemapControlDependency(arg0: TF_ImportGraphDefOptions, arg1: str, arg2: TF_Operation) -> None: ...
def TF_ImportGraphDefOptionsSetPrefix(arg0: TF_ImportGraphDefOptions, arg1: str) -> None: ...
def TF_ImportGraphDefOptionsSetPropagateDeviceSpec(arg0: TF_ImportGraphDefOptions, arg1: int) -> None: ...
def TF_ImportGraphDefOptionsSetUniquifyNames(arg0: TF_ImportGraphDefOptions, arg1: int) -> None: ...
def TF_ImportGraphDefOptionsSetValidateColocationConstraints(arg0: TF_ImportGraphDefOptions, arg1: int) -> None: ...
def TF_ImportGraphDefResultsMissingUnusedInputMappings_wrapper(arg0: TF_ImportGraphDefResults) -> list[str]: ...
def TF_ImportGraphDefResultsReturnOperations(arg0: TF_ImportGraphDefResults) -> list: ...
def TF_ImportGraphDefResultsReturnOutputs(arg0: TF_ImportGraphDefResults) -> list: ...
def TF_LoadLibrary(arg0: str) -> TF_Library: ...
def TF_LoadPluggableDeviceLibrary(arg0: str) -> TF_Library: ...
def TF_NewApiDefMap(arg0: TF_Buffer) -> TF_ApiDefMap: ...
def TF_NewBuffer() -> TF_Buffer: ...
def TF_NewBufferFromString(arg0: bytes) -> TF_Buffer: ...
def TF_NewImportGraphDefOptions() -> TF_ImportGraphDefOptions: ...
def TF_NewOperation(arg0: PyGraph, arg1: str, arg2: str) -> TF_OperationDescription: ...
def TF_NewServer(arg0: bytes) -> TF_Server: ...
def TF_NewSession(arg0: PyGraph, arg1: TF_SessionOptions) -> TF_Session: ...
def TF_NewSessionRef(arg0: PyGraph, arg1: TF_SessionOptions) -> TF_Session: ...
def TF_NewStatus() -> TF_Status: ...
def TF_OperationDevice(arg0: TF_Operation) -> str: ...
def TF_OperationGetAttrBool(arg0: TF_Operation, arg1: str) -> object: ...
def TF_OperationGetAttrInt(arg0: TF_Operation, arg1: str) -> object: ...
def TF_OperationGetAttrType(arg0: TF_Operation, arg1: str) -> TF_DataType: ...
def TF_OperationGetAttrValueProto(arg0: TF_Operation, arg1: str, arg2: TF_Buffer) -> None: ...
def TF_OperationGetControlOutputs_wrapper(arg0: TF_Operation) -> list[TF_Operation]: ...
def TF_OperationGetStackTrace(arg0: TF_Operation) -> object: ...
def TF_OperationInputType(arg0: TF_Input) -> TF_DataType: ...
def TF_OperationName(arg0: TF_Operation) -> str: ...
def TF_OperationNumInputs(arg0: TF_Operation) -> int: ...
def TF_OperationNumOutputs(arg0: TF_Operation) -> int: ...
def TF_OperationOpType(arg0: TF_Operation) -> str: ...
def TF_OperationOutputType(arg0: TF_Output) -> TF_DataType: ...
def TF_OperationToNodeDef(arg0: TF_Operation, arg1: TF_Buffer) -> None: ...
def TF_PluggableDeviceLibraryHandle(arg0: TF_Library) -> None: ...
def TF_RegisterFilesystemPlugin(arg0: str) -> None: ...
def TF_Reset_wrapper(arg0: TF_SessionOptions, arg1: list[bytes]) -> None: ...
def TF_ServerJoin(arg0: TF_Server) -> None: ...
def TF_ServerStart(arg0: TF_Server) -> None: ...
def TF_ServerStop(arg0: TF_Server) -> None: ...
def TF_ServerTarget(arg0: TF_Server) -> str: ...
def TF_SessionListDevices(arg0: TF_Session) -> TF_DeviceList: ...
def TF_SessionMakeCallable(arg0: TF_Session, arg1: TF_Buffer) -> int: ...
def TF_SessionPRunSetup_wrapper(arg0: TF_Session, arg1: list[TF_Output], arg2: list[TF_Output], arg3: list[TF_Operation]) -> str: ...
def TF_SessionPRun_wrapper(arg0: TF_Session, arg1: str, arg2: object, arg3: list[TF_Output]) -> object: ...
def TF_SessionReleaseCallable(arg0: TF_Session, arg1: int) -> None: ...
def TF_SessionRunCallable(arg0: TF_Session, arg1: int, arg2: object, arg3: TF_Buffer) -> list: ...
def TF_SessionRun_wrapper(arg0: TF_Session, arg1: TF_Buffer, arg2: object, arg3: list[TF_Output], arg4: list[TF_Operation], arg5: TF_Buffer) -> object: ...
def TF_SetAttrValueProto(arg0: TF_OperationDescription, arg1: str, arg2: bytes) -> None: ...
def TF_SetDevice(arg0: TF_OperationDescription, arg1: str) -> None: ...
def TF_SetOpStackTrace(arg0: TF_Operation, arg1) -> None: ...
def TF_SetTfXlaCpuGlobalJit(arg0: int) -> int: ...
def TF_SetXlaAutoJitMode(arg0: str) -> None: ...
def TF_SetXlaConstantFoldingDisabled(arg0: int) -> None: ...
def TF_SetXlaEnableLazyCompilation(arg0: int) -> int: ...
def TF_SetXlaMinClusterSize(arg0: int) -> None: ...
def TF_TryEvaluateConstant_wrapper(arg0: PyGraph, arg1: TF_Output) -> object: ...
def UpdateEdge(arg0: PyGraph, arg1: TF_Output, arg2: TF_Input) -> None: ...
def _TF_NewSessionOptions() -> TF_SessionOptions: ...
def _TF_SetConfig(arg0: TF_SessionOptions, arg1: bytes) -> None: ...
def _TF_SetTarget(arg0: TF_SessionOptions, arg1: str) -> None: ...
def get_compiler_version() -> str: ...
def get_cxx11_abi_flag() -> int: ...
def get_cxx_version() -> int: ...
def get_eigen_max_align_bytes() -> int: ...
def get_git_version() -> str: ...
def get_graph_def_version() -> int: ...
def get_graph_def_version_min_consumer() -> int: ...
def get_graph_def_version_min_producer() -> int: ...
def get_monolithic_build() -> int: ...
def get_tensor_handle_key() -> str: ...
def get_version() -> str: ...
