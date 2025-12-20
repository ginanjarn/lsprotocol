from typing import List, Union

from .lsprotocol import (
	ImplementationParams,
	Definition,
	DefinitionLink,
	TypeDefinitionParams,
	WorkspaceFolder,
	ConfigurationParams,
	LSPAny,
	DocumentColorParams,
	ColorInformation,
	ColorPresentationParams,
	ColorPresentation,
	FoldingRangeParams,
	FoldingRange,
	DeclarationParams,
	Declaration,
	DeclarationLink,
	SelectionRangeParams,
	SelectionRange,
	WorkDoneProgressCreateParams,
	CallHierarchyPrepareParams,
	CallHierarchyItem,
	CallHierarchyIncomingCallsParams,
	CallHierarchyIncomingCall,
	CallHierarchyOutgoingCallsParams,
	CallHierarchyOutgoingCall,
	SemanticTokensParams,
	SemanticTokens,
	SemanticTokensDeltaParams,
	SemanticTokensDelta,
	SemanticTokensRangeParams,
	ShowDocumentParams,
	ShowDocumentResult,
	LinkedEditingRangeParams,
	LinkedEditingRanges,
	CreateFilesParams,
	WorkspaceEdit,
	RenameFilesParams,
	DeleteFilesParams,
	MonikerParams,
	Moniker,
	TypeHierarchyPrepareParams,
	TypeHierarchyItem,
	TypeHierarchySupertypesParams,
	TypeHierarchySubtypesParams,
	InlineValueParams,
	InlineValue,
	InlayHintParams,
	InlayHint,
	DocumentDiagnosticParams,
	DocumentDiagnosticReport,
	WorkspaceDiagnosticParams,
	WorkspaceDiagnosticReport,
	InlineCompletionParams,
	InlineCompletionList,
	InlineCompletionItem,
	TextDocumentContentParams,
	TextDocumentContentResult,
	TextDocumentContentRefreshParams,
	RegistrationParams,
	UnregistrationParams,
	InitializeParams,
	InitializeResult,
	ShowMessageRequestParams,
	MessageActionItem,
	WillSaveTextDocumentParams,
	TextEdit,
	CompletionParams,
	CompletionItem,
	CompletionList,
	HoverParams,
	Hover,
	SignatureHelpParams,
	SignatureHelp,
	DefinitionParams,
	ReferenceParams,
	Location,
	DocumentHighlightParams,
	DocumentHighlight,
	DocumentSymbolParams,
	SymbolInformation,
	DocumentSymbol,
	CodeActionParams,
	Command,
	CodeAction,
	WorkspaceSymbolParams,
	WorkspaceSymbol,
	CodeLensParams,
	CodeLens,
	DocumentLinkParams,
	DocumentLink,
	DocumentFormattingParams,
	DocumentRangeFormattingParams,
	DocumentRangesFormattingParams,
	DocumentOnTypeFormattingParams,
	RenameParams,
	PrepareRenameParams,
	PrepareRenameResult,
	ExecuteCommandParams,
	ApplyWorkspaceEditParams,
	ApplyWorkspaceEditResult,
	DidChangeWorkspaceFoldersParams,
	WorkDoneProgressCancelParams,
	DidOpenNotebookDocumentParams,
	DidChangeNotebookDocumentParams,
	DidSaveNotebookDocumentParams,
	DidCloseNotebookDocumentParams,
	InitializedParams,
	DidChangeConfigurationParams,
	ShowMessageParams,
	LogMessageParams,
	DidOpenTextDocumentParams,
	DidChangeTextDocumentParams,
	DidCloseTextDocumentParams,
	DidSaveTextDocumentParams,
	DidChangeWatchedFilesParams,
	PublishDiagnosticsParams,
	SetTraceParams,
	LogTraceParams,
	CancelParams,
	ProgressParams
)

class Server:
	def handle_implementation_request(self, context: dict, params: ImplementationParams) -> Union[Definition, List[DefinitionLink], None]:
		""""""

	def handle_type_definition_request(self, context: dict, params: TypeDefinitionParams) -> Union[Definition, List[DefinitionLink], None]:
		""""""

	def workspace_folders_request(self, params: None) -> None:
		"""The `workspace/workspaceFolders` is sent from the server to the client to fetch the open workspace folders."""
		self.request(method='workspace/workspaceFolders', params=params)

	def handle_workspace_folders_request(self, context: dict, result: Union[List[WorkspaceFolder], None]) -> None:
		""""""

	def configuration_request(self, params: ConfigurationParams) -> None:
		"""The 'workspace/configuration' request is sent from the server to the client to fetch a certain
		configuration setting.

		This pull model replaces the old push model were the client signaled configuration change via an
		event. If the server still needs to react to configuration changes (since the server caches the
		result of `workspace/configuration` requests) the server should register for an empty configuration
		change event and empty the cache if such an event is received."""
		self.request(method='workspace/configuration', params=params)

	def handle_configuration_request(self, context: dict, result: List[LSPAny]) -> None:
		""""""

	def handle_document_color_request(self, context: dict, params: DocumentColorParams) -> List[ColorInformation]:
		""""""

	def handle_color_presentation_request(self, context: dict, params: ColorPresentationParams) -> List[ColorPresentation]:
		""""""

	def handle_folding_range_request(self, context: dict, params: FoldingRangeParams) -> Union[List[FoldingRange], None]:
		""""""

	def folding_range_refresh_request(self, params: None) -> None:
		"""@since 3.18.0
		@proposed"""
		self.request(method='workspace/foldingRange/refresh', params=params)

	def handle_folding_range_refresh_request(self, context: dict, result: None) -> None:
		""""""

	def handle_declaration_request(self, context: dict, params: DeclarationParams) -> Union[Declaration, List[DeclarationLink], None]:
		""""""

	def handle_selection_range_request(self, context: dict, params: SelectionRangeParams) -> Union[List[SelectionRange], None]:
		""""""

	def work_done_progress_create_request(self, params: WorkDoneProgressCreateParams) -> None:
		"""The `window/workDoneProgress/create` request is sent from the server to the client to initiate progress
		reporting from the server."""
		self.request(method='window/workDoneProgress/create', params=params)

	def handle_work_done_progress_create_request(self, context: dict, result: None) -> None:
		""""""

	def handle_call_hierarchy_prepare_request(self, context: dict, params: CallHierarchyPrepareParams) -> Union[List[CallHierarchyItem], None]:
		""""""

	def handle_call_hierarchy_incoming_calls_request(self, context: dict, params: CallHierarchyIncomingCallsParams) -> Union[List[CallHierarchyIncomingCall], None]:
		""""""

	def handle_call_hierarchy_outgoing_calls_request(self, context: dict, params: CallHierarchyOutgoingCallsParams) -> Union[List[CallHierarchyOutgoingCall], None]:
		""""""

	def handle_semantic_tokens_request(self, context: dict, params: SemanticTokensParams) -> Union[SemanticTokens, None]:
		""""""

	def handle_semantic_tokens_delta_request(self, context: dict, params: SemanticTokensDeltaParams) -> Union[SemanticTokens, SemanticTokensDelta, None]:
		""""""

	def handle_semantic_tokens_range_request(self, context: dict, params: SemanticTokensRangeParams) -> Union[SemanticTokens, None]:
		""""""

	def semantic_tokens_refresh_request(self, params: None) -> None:
		"""@since 3.16.0"""
		self.request(method='workspace/semanticTokens/refresh', params=params)

	def handle_semantic_tokens_refresh_request(self, context: dict, result: None) -> None:
		""""""

	def show_document_request(self, params: ShowDocumentParams) -> None:
		"""A request to show a document. This request might open an
		external program depending on the value of the URI to open.
		For example a request to open `https://code.visualstudio.com/`
		will very likely open the URI in a WEB browser.

		@since 3.16.0"""
		self.request(method='window/showDocument', params=params)

	def handle_show_document_request(self, context: dict, result: ShowDocumentResult) -> None:
		""""""

	def handle_linked_editing_range_request(self, context: dict, params: LinkedEditingRangeParams) -> Union[LinkedEditingRanges, None]:
		""""""

	def handle_will_create_files_request(self, context: dict, params: CreateFilesParams) -> Union[WorkspaceEdit, None]:
		""""""

	def handle_will_rename_files_request(self, context: dict, params: RenameFilesParams) -> Union[WorkspaceEdit, None]:
		""""""

	def handle_will_delete_files_request(self, context: dict, params: DeleteFilesParams) -> Union[WorkspaceEdit, None]:
		""""""

	def handle_moniker_request(self, context: dict, params: MonikerParams) -> Union[List[Moniker], None]:
		""""""

	def handle_type_hierarchy_prepare_request(self, context: dict, params: TypeHierarchyPrepareParams) -> Union[List[TypeHierarchyItem], None]:
		""""""

	def handle_type_hierarchy_supertypes_request(self, context: dict, params: TypeHierarchySupertypesParams) -> Union[List[TypeHierarchyItem], None]:
		""""""

	def handle_type_hierarchy_subtypes_request(self, context: dict, params: TypeHierarchySubtypesParams) -> Union[List[TypeHierarchyItem], None]:
		""""""

	def handle_inline_value_request(self, context: dict, params: InlineValueParams) -> Union[List[InlineValue], None]:
		""""""

	def inline_value_refresh_request(self, params: None) -> None:
		"""@since 3.17.0"""
		self.request(method='workspace/inlineValue/refresh', params=params)

	def handle_inline_value_refresh_request(self, context: dict, result: None) -> None:
		""""""

	def handle_inlay_hint_request(self, context: dict, params: InlayHintParams) -> Union[List[InlayHint], None]:
		""""""

	def handle_inlay_hint_resolve_request(self, context: dict, params: InlayHint) -> InlayHint:
		""""""

	def inlay_hint_refresh_request(self, params: None) -> None:
		"""@since 3.17.0"""
		self.request(method='workspace/inlayHint/refresh', params=params)

	def handle_inlay_hint_refresh_request(self, context: dict, result: None) -> None:
		""""""

	def handle_document_diagnostic_request(self, context: dict, params: DocumentDiagnosticParams) -> DocumentDiagnosticReport:
		""""""

	def handle_workspace_diagnostic_request(self, context: dict, params: WorkspaceDiagnosticParams) -> WorkspaceDiagnosticReport:
		""""""

	def diagnostic_refresh_request(self, params: None) -> None:
		"""The diagnostic refresh request definition.

		@since 3.17.0"""
		self.request(method='workspace/diagnostic/refresh', params=params)

	def handle_diagnostic_refresh_request(self, context: dict, result: None) -> None:
		""""""

	def handle_inline_completion_request(self, context: dict, params: InlineCompletionParams) -> Union[InlineCompletionList, List[InlineCompletionItem], None]:
		""""""

	def handle_text_document_content_request(self, context: dict, params: TextDocumentContentParams) -> TextDocumentContentResult:
		""""""

	def text_document_content_refresh_request(self, params: TextDocumentContentRefreshParams) -> None:
		"""The `workspace/textDocumentContent` request is sent from the server to the client to refresh
		the content of a specific text document.

		@since 3.18.0
		@proposed"""
		self.request(method='workspace/textDocumentContent/refresh', params=params)

	def handle_text_document_content_refresh_request(self, context: dict, result: None) -> None:
		""""""

	def registration_request(self, params: RegistrationParams) -> None:
		"""The `client/registerCapability` request is sent from the server to the client to register a new capability
		handler on the client side."""
		self.request(method='client/registerCapability', params=params)

	def handle_registration_request(self, context: dict, result: None) -> None:
		""""""

	def unregistration_request(self, params: UnregistrationParams) -> None:
		"""The `client/unregisterCapability` request is sent from the server to the client to unregister a previously registered capability
		handler on the client side."""
		self.request(method='client/unregisterCapability', params=params)

	def handle_unregistration_request(self, context: dict, result: None) -> None:
		""""""

	def handle_initialize_request(self, context: dict, params: InitializeParams) -> InitializeResult:
		""""""

	def handle_shutdown_request(self, context: dict, params: None) -> None:
		""""""

	def show_message_request(self, params: ShowMessageRequestParams) -> None:
		"""The show message request is sent from the server to the client to show a message
		and a set of options actions to the user."""
		self.request(method='window/showMessageRequest', params=params)

	def handle_show_message_request(self, context: dict, result: Union[MessageActionItem, None]) -> None:
		""""""

	def handle_will_save_text_document_wait_until_request(self, context: dict, params: WillSaveTextDocumentParams) -> Union[List[TextEdit], None]:
		""""""

	def handle_completion_request(self, context: dict, params: CompletionParams) -> Union[List[CompletionItem], CompletionList, None]:
		""""""

	def handle_completion_resolve_request(self, context: dict, params: CompletionItem) -> CompletionItem:
		""""""

	def handle_hover_request(self, context: dict, params: HoverParams) -> Union[Hover, None]:
		""""""

	def handle_signature_help_request(self, context: dict, params: SignatureHelpParams) -> Union[SignatureHelp, None]:
		""""""

	def handle_definition_request(self, context: dict, params: DefinitionParams) -> Union[Definition, List[DefinitionLink], None]:
		""""""

	def handle_references_request(self, context: dict, params: ReferenceParams) -> Union[List[Location], None]:
		""""""

	def handle_document_highlight_request(self, context: dict, params: DocumentHighlightParams) -> Union[List[DocumentHighlight], None]:
		""""""

	def handle_document_symbol_request(self, context: dict, params: DocumentSymbolParams) -> Union[List[SymbolInformation], List[DocumentSymbol], None]:
		""""""

	def handle_code_action_request(self, context: dict, params: CodeActionParams) -> Union[List[Union[Command, CodeAction]], None]:
		""""""

	def handle_code_action_resolve_request(self, context: dict, params: CodeAction) -> CodeAction:
		""""""

	def handle_workspace_symbol_request(self, context: dict, params: WorkspaceSymbolParams) -> Union[List[SymbolInformation], List[WorkspaceSymbol], None]:
		""""""

	def handle_workspace_symbol_resolve_request(self, context: dict, params: WorkspaceSymbol) -> WorkspaceSymbol:
		""""""

	def handle_code_lens_request(self, context: dict, params: CodeLensParams) -> Union[List[CodeLens], None]:
		""""""

	def handle_code_lens_resolve_request(self, context: dict, params: CodeLens) -> CodeLens:
		""""""

	def code_lens_refresh_request(self, params: None) -> None:
		"""A request to refresh all code actions

		@since 3.16.0"""
		self.request(method='workspace/codeLens/refresh', params=params)

	def handle_code_lens_refresh_request(self, context: dict, result: None) -> None:
		""""""

	def handle_document_link_request(self, context: dict, params: DocumentLinkParams) -> Union[List[DocumentLink], None]:
		""""""

	def handle_document_link_resolve_request(self, context: dict, params: DocumentLink) -> DocumentLink:
		""""""

	def handle_document_formatting_request(self, context: dict, params: DocumentFormattingParams) -> Union[List[TextEdit], None]:
		""""""

	def handle_document_range_formatting_request(self, context: dict, params: DocumentRangeFormattingParams) -> Union[List[TextEdit], None]:
		""""""

	def handle_document_ranges_formatting_request(self, context: dict, params: DocumentRangesFormattingParams) -> Union[List[TextEdit], None]:
		""""""

	def handle_document_on_type_formatting_request(self, context: dict, params: DocumentOnTypeFormattingParams) -> Union[List[TextEdit], None]:
		""""""

	def handle_rename_request(self, context: dict, params: RenameParams) -> Union[WorkspaceEdit, None]:
		""""""

	def handle_prepare_rename_request(self, context: dict, params: PrepareRenameParams) -> Union[PrepareRenameResult, None]:
		""""""

	def handle_execute_command_request(self, context: dict, params: ExecuteCommandParams) -> Union[LSPAny, None]:
		""""""

	def apply_workspace_edit_request(self, params: ApplyWorkspaceEditParams) -> None:
		"""A request sent from the server to the client to modified certain resources."""
		self.request(method='workspace/applyEdit', params=params)

	def handle_apply_workspace_edit_request(self, context: dict, result: ApplyWorkspaceEditResult) -> None:
		""""""

	def handle_did_change_workspace_folders_notification(self, context: dict, params: DidChangeWorkspaceFoldersParams) -> None:
		""""""

	def handle_work_done_progress_cancel_notification(self, context: dict, params: WorkDoneProgressCancelParams) -> None:
		""""""

	def handle_did_create_files_notification(self, context: dict, params: CreateFilesParams) -> None:
		""""""

	def handle_did_rename_files_notification(self, context: dict, params: RenameFilesParams) -> None:
		""""""

	def handle_did_delete_files_notification(self, context: dict, params: DeleteFilesParams) -> None:
		""""""

	def handle_did_open_notebook_document_notification(self, context: dict, params: DidOpenNotebookDocumentParams) -> None:
		""""""

	def handle_did_change_notebook_document_notification(self, context: dict, params: DidChangeNotebookDocumentParams) -> None:
		""""""

	def handle_did_save_notebook_document_notification(self, context: dict, params: DidSaveNotebookDocumentParams) -> None:
		""""""

	def handle_did_close_notebook_document_notification(self, context: dict, params: DidCloseNotebookDocumentParams) -> None:
		""""""

	def handle_initialized_notification(self, context: dict, params: InitializedParams) -> None:
		""""""

	def handle_exit_notification(self, context: dict, params: None) -> None:
		""""""

	def handle_did_change_configuration_notification(self, context: dict, params: DidChangeConfigurationParams) -> None:
		""""""

	def show_message_notification(self, params: ShowMessageParams) -> None:
		"""The show message notification is sent from a server to a client to ask
		the client to display a particular message in the user interface."""
		self.notify(method='window/showMessage', params=params)

	def log_message_notification(self, params: LogMessageParams) -> None:
		"""The log message notification is sent from the server to the client to ask
		the client to log a particular message."""
		self.notify(method='window/logMessage', params=params)

	def telemetry_event_notification(self, params: LSPAny) -> None:
		"""The telemetry event notification is sent from the server to the client to ask
		the client to log telemetry data."""
		self.notify(method='telemetry/event', params=params)

	def handle_did_open_text_document_notification(self, context: dict, params: DidOpenTextDocumentParams) -> None:
		""""""

	def handle_did_change_text_document_notification(self, context: dict, params: DidChangeTextDocumentParams) -> None:
		""""""

	def handle_did_close_text_document_notification(self, context: dict, params: DidCloseTextDocumentParams) -> None:
		""""""

	def handle_did_save_text_document_notification(self, context: dict, params: DidSaveTextDocumentParams) -> None:
		""""""

	def handle_will_save_text_document_notification(self, context: dict, params: WillSaveTextDocumentParams) -> None:
		""""""

	def handle_did_change_watched_files_notification(self, context: dict, params: DidChangeWatchedFilesParams) -> None:
		""""""

	def publish_diagnostics_notification(self, params: PublishDiagnosticsParams) -> None:
		"""Diagnostics notification are sent from the server to the client to signal
		results of validation runs."""
		self.notify(method='textDocument/publishDiagnostics', params=params)

	def handle_set_trace_notification(self, context: dict, params: SetTraceParams) -> None:
		""""""

	def log_trace_notification(self, params: LogTraceParams) -> None:
		self.notify(method='$/logTrace', params=params)

	def handle_cancel_notification(self, context: dict, params: CancelParams) -> None:
		""""""

	def cancel_notification(self, params: CancelParams) -> None:
		self.notify(method='$/cancelRequest', params=params)

	def handle_progress_notification(self, context: dict, params: ProgressParams) -> None:
		""""""

	def progress_notification(self, params: ProgressParams) -> None:
		self.notify(method='$/progress', params=params)

	def handle(self, method: str, params_or_result: LSPAny) -> None:
		handle_map = {
			'textDocument/implementation': self.handle_implementation_request,
			'textDocument/typeDefinition': self.handle_type_definition_request,
			'workspace/workspaceFolders': self.handle_workspace_folders_request,
			'workspace/configuration': self.handle_configuration_request,
			'textDocument/documentColor': self.handle_document_color_request,
			'textDocument/colorPresentation': self.handle_color_presentation_request,
			'textDocument/foldingRange': self.handle_folding_range_request,
			'workspace/foldingRange/refresh': self.handle_folding_range_refresh_request,
			'textDocument/declaration': self.handle_declaration_request,
			'textDocument/selectionRange': self.handle_selection_range_request,
			'window/workDoneProgress/create': self.handle_work_done_progress_create_request,
			'textDocument/prepareCallHierarchy': self.handle_call_hierarchy_prepare_request,
			'callHierarchy/incomingCalls': self.handle_call_hierarchy_incoming_calls_request,
			'callHierarchy/outgoingCalls': self.handle_call_hierarchy_outgoing_calls_request,
			'textDocument/semanticTokens/full': self.handle_semantic_tokens_request,
			'textDocument/semanticTokens/full/delta': self.handle_semantic_tokens_delta_request,
			'textDocument/semanticTokens/range': self.handle_semantic_tokens_range_request,
			'workspace/semanticTokens/refresh': self.handle_semantic_tokens_refresh_request,
			'window/showDocument': self.handle_show_document_request,
			'textDocument/linkedEditingRange': self.handle_linked_editing_range_request,
			'workspace/willCreateFiles': self.handle_will_create_files_request,
			'workspace/willRenameFiles': self.handle_will_rename_files_request,
			'workspace/willDeleteFiles': self.handle_will_delete_files_request,
			'textDocument/moniker': self.handle_moniker_request,
			'textDocument/prepareTypeHierarchy': self.handle_type_hierarchy_prepare_request,
			'typeHierarchy/supertypes': self.handle_type_hierarchy_supertypes_request,
			'typeHierarchy/subtypes': self.handle_type_hierarchy_subtypes_request,
			'textDocument/inlineValue': self.handle_inline_value_request,
			'workspace/inlineValue/refresh': self.handle_inline_value_refresh_request,
			'textDocument/inlayHint': self.handle_inlay_hint_request,
			'inlayHint/resolve': self.handle_inlay_hint_resolve_request,
			'workspace/inlayHint/refresh': self.handle_inlay_hint_refresh_request,
			'textDocument/diagnostic': self.handle_document_diagnostic_request,
			'workspace/diagnostic': self.handle_workspace_diagnostic_request,
			'workspace/diagnostic/refresh': self.handle_diagnostic_refresh_request,
			'textDocument/inlineCompletion': self.handle_inline_completion_request,
			'workspace/textDocumentContent': self.handle_text_document_content_request,
			'workspace/textDocumentContent/refresh': self.handle_text_document_content_refresh_request,
			'client/registerCapability': self.handle_registration_request,
			'client/unregisterCapability': self.handle_unregistration_request,
			'initialize': self.handle_initialize_request,
			'shutdown': self.handle_shutdown_request,
			'window/showMessageRequest': self.handle_show_message_request,
			'textDocument/willSaveWaitUntil': self.handle_will_save_text_document_wait_until_request,
			'textDocument/completion': self.handle_completion_request,
			'completionItem/resolve': self.handle_completion_resolve_request,
			'textDocument/hover': self.handle_hover_request,
			'textDocument/signatureHelp': self.handle_signature_help_request,
			'textDocument/definition': self.handle_definition_request,
			'textDocument/references': self.handle_references_request,
			'textDocument/documentHighlight': self.handle_document_highlight_request,
			'textDocument/documentSymbol': self.handle_document_symbol_request,
			'textDocument/codeAction': self.handle_code_action_request,
			'codeAction/resolve': self.handle_code_action_resolve_request,
			'workspace/symbol': self.handle_workspace_symbol_request,
			'workspaceSymbol/resolve': self.handle_workspace_symbol_resolve_request,
			'textDocument/codeLens': self.handle_code_lens_request,
			'codeLens/resolve': self.handle_code_lens_resolve_request,
			'workspace/codeLens/refresh': self.handle_code_lens_refresh_request,
			'textDocument/documentLink': self.handle_document_link_request,
			'documentLink/resolve': self.handle_document_link_resolve_request,
			'textDocument/formatting': self.handle_document_formatting_request,
			'textDocument/rangeFormatting': self.handle_document_range_formatting_request,
			'textDocument/rangesFormatting': self.handle_document_ranges_formatting_request,
			'textDocument/onTypeFormatting': self.handle_document_on_type_formatting_request,
			'textDocument/rename': self.handle_rename_request,
			'textDocument/prepareRename': self.handle_prepare_rename_request,
			'workspace/executeCommand': self.handle_execute_command_request,
			'workspace/applyEdit': self.handle_apply_workspace_edit_request,
			'workspace/didChangeWorkspaceFolders': self.handle_did_change_workspace_folders_notification,
			'window/workDoneProgress/cancel': self.handle_work_done_progress_cancel_notification,
			'workspace/didCreateFiles': self.handle_did_create_files_notification,
			'workspace/didRenameFiles': self.handle_did_rename_files_notification,
			'workspace/didDeleteFiles': self.handle_did_delete_files_notification,
			'notebookDocument/didOpen': self.handle_did_open_notebook_document_notification,
			'notebookDocument/didChange': self.handle_did_change_notebook_document_notification,
			'notebookDocument/didSave': self.handle_did_save_notebook_document_notification,
			'notebookDocument/didClose': self.handle_did_close_notebook_document_notification,
			'initialized': self.handle_initialized_notification,
			'exit': self.handle_exit_notification,
			'workspace/didChangeConfiguration': self.handle_did_change_configuration_notification,
			'textDocument/didOpen': self.handle_did_open_text_document_notification,
			'textDocument/didChange': self.handle_did_change_text_document_notification,
			'textDocument/didClose': self.handle_did_close_text_document_notification,
			'textDocument/didSave': self.handle_did_save_text_document_notification,
			'textDocument/willSave': self.handle_will_save_text_document_notification,
			'workspace/didChangeWatchedFiles': self.handle_did_change_watched_files_notification,
			'$/setTrace': self.handle_set_trace_notification,
			'$/cancelRequest': self.handle_cancel_notification,
			'$/progress': self.handle_progress_notification
			}
		return handle_map[method](params_or_result)

