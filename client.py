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

class Client:
	def implementation_request(self, params: ImplementationParams) -> None:
		"""A request to resolve the implementation locations of a symbol at a given text
		document position. The request's parameter is of type {@link TextDocumentPositionParams}
		the response is of type {@link Definition} or a Thenable that resolves to such."""
		self.request(method='textDocument/implementation', params=params)

	def handle_implementation_request(self, context: dict, result: Union[Definition, List[DefinitionLink], None]) -> None:
		""""""

	def type_definition_request(self, params: TypeDefinitionParams) -> None:
		"""A request to resolve the type definition locations of a symbol at a given text
		document position. The request's parameter is of type {@link TextDocumentPositionParams}
		the response is of type {@link Definition} or a Thenable that resolves to such."""
		self.request(method='textDocument/typeDefinition', params=params)

	def handle_type_definition_request(self, context: dict, result: Union[Definition, List[DefinitionLink], None]) -> None:
		""""""

	def handle_workspace_folders_request(self, context: dict, params: None) -> Union[List[WorkspaceFolder], None]:
		""""""

	def handle_configuration_request(self, context: dict, params: ConfigurationParams) -> List[LSPAny]:
		""""""

	def document_color_request(self, params: DocumentColorParams) -> None:
		"""A request to list all color symbols found in a given text document. The request's
		parameter is of type {@link DocumentColorParams} the
		response is of type {@link ColorInformation ColorInformation[]} or a Thenable
		that resolves to such."""
		self.request(method='textDocument/documentColor', params=params)

	def handle_document_color_request(self, context: dict, result: List[ColorInformation]) -> None:
		""""""

	def color_presentation_request(self, params: ColorPresentationParams) -> None:
		"""A request to list all presentation for a color. The request's
		parameter is of type {@link ColorPresentationParams} the
		response is of type {@link ColorInformation ColorInformation[]} or a Thenable
		that resolves to such."""
		self.request(method='textDocument/colorPresentation', params=params)

	def handle_color_presentation_request(self, context: dict, result: List[ColorPresentation]) -> None:
		""""""

	def folding_range_request(self, params: FoldingRangeParams) -> None:
		"""A request to provide folding ranges in a document. The request's
		parameter is of type {@link FoldingRangeParams}, the
		response is of type {@link FoldingRangeList} or a Thenable
		that resolves to such."""
		self.request(method='textDocument/foldingRange', params=params)

	def handle_folding_range_request(self, context: dict, result: Union[List[FoldingRange], None]) -> None:
		""""""

	def handle_folding_range_refresh_request(self, context: dict, params: None) -> None:
		""""""

	def declaration_request(self, params: DeclarationParams) -> None:
		"""A request to resolve the type definition locations of a symbol at a given text
		document position. The request's parameter is of type {@link TextDocumentPositionParams}
		the response is of type {@link Declaration} or a typed array of {@link DeclarationLink}
		or a Thenable that resolves to such."""
		self.request(method='textDocument/declaration', params=params)

	def handle_declaration_request(self, context: dict, result: Union[Declaration, List[DeclarationLink], None]) -> None:
		""""""

	def selection_range_request(self, params: SelectionRangeParams) -> None:
		"""A request to provide selection ranges in a document. The request's
		parameter is of type {@link SelectionRangeParams}, the
		response is of type {@link SelectionRange SelectionRange[]} or a Thenable
		that resolves to such."""
		self.request(method='textDocument/selectionRange', params=params)

	def handle_selection_range_request(self, context: dict, result: Union[List[SelectionRange], None]) -> None:
		""""""

	def handle_work_done_progress_create_request(self, context: dict, params: WorkDoneProgressCreateParams) -> None:
		""""""

	def call_hierarchy_prepare_request(self, params: CallHierarchyPrepareParams) -> None:
		"""A request to result a `CallHierarchyItem` in a document at a given position.
		Can be used as an input to an incoming or outgoing call hierarchy.

		@since 3.16.0"""
		self.request(method='textDocument/prepareCallHierarchy', params=params)

	def handle_call_hierarchy_prepare_request(self, context: dict, result: Union[List[CallHierarchyItem], None]) -> None:
		""""""

	def call_hierarchy_incoming_calls_request(self, params: CallHierarchyIncomingCallsParams) -> None:
		"""A request to resolve the incoming calls for a given `CallHierarchyItem`.

		@since 3.16.0"""
		self.request(method='callHierarchy/incomingCalls', params=params)

	def handle_call_hierarchy_incoming_calls_request(self, context: dict, result: Union[List[CallHierarchyIncomingCall], None]) -> None:
		""""""

	def call_hierarchy_outgoing_calls_request(self, params: CallHierarchyOutgoingCallsParams) -> None:
		"""A request to resolve the outgoing calls for a given `CallHierarchyItem`.

		@since 3.16.0"""
		self.request(method='callHierarchy/outgoingCalls', params=params)

	def handle_call_hierarchy_outgoing_calls_request(self, context: dict, result: Union[List[CallHierarchyOutgoingCall], None]) -> None:
		""""""

	def semantic_tokens_request(self, params: SemanticTokensParams) -> None:
		"""@since 3.16.0"""
		self.request(method='textDocument/semanticTokens/full', params=params)

	def handle_semantic_tokens_request(self, context: dict, result: Union[SemanticTokens, None]) -> None:
		""""""

	def semantic_tokens_delta_request(self, params: SemanticTokensDeltaParams) -> None:
		"""@since 3.16.0"""
		self.request(method='textDocument/semanticTokens/full/delta', params=params)

	def handle_semantic_tokens_delta_request(self, context: dict, result: Union[SemanticTokens, SemanticTokensDelta, None]) -> None:
		""""""

	def semantic_tokens_range_request(self, params: SemanticTokensRangeParams) -> None:
		"""@since 3.16.0"""
		self.request(method='textDocument/semanticTokens/range', params=params)

	def handle_semantic_tokens_range_request(self, context: dict, result: Union[SemanticTokens, None]) -> None:
		""""""

	def handle_semantic_tokens_refresh_request(self, context: dict, params: None) -> None:
		""""""

	def handle_show_document_request(self, context: dict, params: ShowDocumentParams) -> ShowDocumentResult:
		""""""

	def linked_editing_range_request(self, params: LinkedEditingRangeParams) -> None:
		"""A request to provide ranges that can be edited together.

		@since 3.16.0"""
		self.request(method='textDocument/linkedEditingRange', params=params)

	def handle_linked_editing_range_request(self, context: dict, result: Union[LinkedEditingRanges, None]) -> None:
		""""""

	def will_create_files_request(self, params: CreateFilesParams) -> None:
		"""The will create files request is sent from the client to the server before files are actually
		created as long as the creation is triggered from within the client.

		The request can return a `WorkspaceEdit` which will be applied to workspace before the
		files are created. Hence the `WorkspaceEdit` can not manipulate the content of the file
		to be created.

		@since 3.16.0"""
		self.request(method='workspace/willCreateFiles', params=params)

	def handle_will_create_files_request(self, context: dict, result: Union[WorkspaceEdit, None]) -> None:
		""""""

	def will_rename_files_request(self, params: RenameFilesParams) -> None:
		"""The will rename files request is sent from the client to the server before files are actually
		renamed as long as the rename is triggered from within the client.

		@since 3.16.0"""
		self.request(method='workspace/willRenameFiles', params=params)

	def handle_will_rename_files_request(self, context: dict, result: Union[WorkspaceEdit, None]) -> None:
		""""""

	def will_delete_files_request(self, params: DeleteFilesParams) -> None:
		"""The did delete files notification is sent from the client to the server when
		files were deleted from within the client.

		@since 3.16.0"""
		self.request(method='workspace/willDeleteFiles', params=params)

	def handle_will_delete_files_request(self, context: dict, result: Union[WorkspaceEdit, None]) -> None:
		""""""

	def moniker_request(self, params: MonikerParams) -> None:
		"""A request to get the moniker of a symbol at a given text document position.
		The request parameter is of type {@link TextDocumentPositionParams}.
		The response is of type {@link Moniker Moniker[]} or `null`."""
		self.request(method='textDocument/moniker', params=params)

	def handle_moniker_request(self, context: dict, result: Union[List[Moniker], None]) -> None:
		""""""

	def type_hierarchy_prepare_request(self, params: TypeHierarchyPrepareParams) -> None:
		"""A request to result a `TypeHierarchyItem` in a document at a given position.
		Can be used as an input to a subtypes or supertypes type hierarchy.

		@since 3.17.0"""
		self.request(method='textDocument/prepareTypeHierarchy', params=params)

	def handle_type_hierarchy_prepare_request(self, context: dict, result: Union[List[TypeHierarchyItem], None]) -> None:
		""""""

	def type_hierarchy_supertypes_request(self, params: TypeHierarchySupertypesParams) -> None:
		"""A request to resolve the supertypes for a given `TypeHierarchyItem`.

		@since 3.17.0"""
		self.request(method='typeHierarchy/supertypes', params=params)

	def handle_type_hierarchy_supertypes_request(self, context: dict, result: Union[List[TypeHierarchyItem], None]) -> None:
		""""""

	def type_hierarchy_subtypes_request(self, params: TypeHierarchySubtypesParams) -> None:
		"""A request to resolve the subtypes for a given `TypeHierarchyItem`.

		@since 3.17.0"""
		self.request(method='typeHierarchy/subtypes', params=params)

	def handle_type_hierarchy_subtypes_request(self, context: dict, result: Union[List[TypeHierarchyItem], None]) -> None:
		""""""

	def inline_value_request(self, params: InlineValueParams) -> None:
		"""A request to provide inline values in a document. The request's parameter is of
		type {@link InlineValueParams}, the response is of type
		{@link InlineValue InlineValue[]} or a Thenable that resolves to such.

		@since 3.17.0"""
		self.request(method='textDocument/inlineValue', params=params)

	def handle_inline_value_request(self, context: dict, result: Union[List[InlineValue], None]) -> None:
		""""""

	def handle_inline_value_refresh_request(self, context: dict, params: None) -> None:
		""""""

	def inlay_hint_request(self, params: InlayHintParams) -> None:
		"""A request to provide inlay hints in a document. The request's parameter is of
		type {@link InlayHintsParams}, the response is of type
		{@link InlayHint InlayHint[]} or a Thenable that resolves to such.

		@since 3.17.0"""
		self.request(method='textDocument/inlayHint', params=params)

	def handle_inlay_hint_request(self, context: dict, result: Union[List[InlayHint], None]) -> None:
		""""""

	def inlay_hint_resolve_request(self, params: InlayHint) -> None:
		"""A request to resolve additional properties for an inlay hint.
		The request's parameter is of type {@link InlayHint}, the response is
		of type {@link InlayHint} or a Thenable that resolves to such.

		@since 3.17.0"""
		self.request(method='inlayHint/resolve', params=params)

	def handle_inlay_hint_resolve_request(self, context: dict, result: InlayHint) -> None:
		""""""

	def handle_inlay_hint_refresh_request(self, context: dict, params: None) -> None:
		""""""

	def document_diagnostic_request(self, params: DocumentDiagnosticParams) -> None:
		"""The document diagnostic request definition.

		@since 3.17.0"""
		self.request(method='textDocument/diagnostic', params=params)

	def handle_document_diagnostic_request(self, context: dict, result: DocumentDiagnosticReport) -> None:
		""""""

	def workspace_diagnostic_request(self, params: WorkspaceDiagnosticParams) -> None:
		"""The workspace diagnostic request definition.

		@since 3.17.0"""
		self.request(method='workspace/diagnostic', params=params)

	def handle_workspace_diagnostic_request(self, context: dict, result: WorkspaceDiagnosticReport) -> None:
		""""""

	def handle_diagnostic_refresh_request(self, context: dict, params: None) -> None:
		""""""

	def inline_completion_request(self, params: InlineCompletionParams) -> None:
		"""A request to provide inline completions in a document. The request's parameter is of
		type {@link InlineCompletionParams}, the response is of type
		{@link InlineCompletion InlineCompletion[]} or a Thenable that resolves to such.

		@since 3.18.0
		@proposed"""
		self.request(method='textDocument/inlineCompletion', params=params)

	def handle_inline_completion_request(self, context: dict, result: Union[InlineCompletionList, List[InlineCompletionItem], None]) -> None:
		""""""

	def text_document_content_request(self, params: TextDocumentContentParams) -> None:
		"""The `workspace/textDocumentContent` request is sent from the client to the
		server to request the content of a text document.

		@since 3.18.0
		@proposed"""
		self.request(method='workspace/textDocumentContent', params=params)

	def handle_text_document_content_request(self, context: dict, result: TextDocumentContentResult) -> None:
		""""""

	def handle_text_document_content_refresh_request(self, context: dict, params: TextDocumentContentRefreshParams) -> None:
		""""""

	def handle_registration_request(self, context: dict, params: RegistrationParams) -> None:
		""""""

	def handle_unregistration_request(self, context: dict, params: UnregistrationParams) -> None:
		""""""

	def initialize_request(self, params: InitializeParams) -> None:
		"""The initialize request is sent from the client to the server.
		It is sent once as the request after starting up the server.
		The requests parameter is of type {@link InitializeParams}
		the response if of type {@link InitializeResult} of a Thenable that
		resolves to such."""
		self.request(method='initialize', params=params)

	def handle_initialize_request(self, context: dict, result: InitializeResult) -> None:
		""""""

	def shutdown_request(self, params: None) -> None:
		"""A shutdown request is sent from the client to the server.
		It is sent once when the client decides to shutdown the
		server. The only notification that is sent after a shutdown request
		is the exit event."""
		self.request(method='shutdown', params=params)

	def handle_shutdown_request(self, context: dict, result: None) -> None:
		""""""

	def handle_show_message_request(self, context: dict, params: ShowMessageRequestParams) -> Union[MessageActionItem, None]:
		""""""

	def will_save_text_document_wait_until_request(self, params: WillSaveTextDocumentParams) -> None:
		"""A document will save request is sent from the client to the server before
		the document is actually saved. The request can return an array of TextEdits
		which will be applied to the text document before it is saved. Please note that
		clients might drop results if computing the text edits took too long or if a
		server constantly fails on this request. This is done to keep the save fast and
		reliable."""
		self.request(method='textDocument/willSaveWaitUntil', params=params)

	def handle_will_save_text_document_wait_until_request(self, context: dict, result: Union[List[TextEdit], None]) -> None:
		""""""

	def completion_request(self, params: CompletionParams) -> None:
		"""Request to request completion at a given text document position. The request's
		parameter is of type {@link TextDocumentPosition} the response
		is of type {@link CompletionItem CompletionItem[]} or {@link CompletionList}
		or a Thenable that resolves to such.

		The request can delay the computation of the {@link CompletionItem.detail `detail`}
		and {@link CompletionItem.documentation `documentation`} properties to the `completionItem/resolve`
		request. However, properties that are needed for the initial sorting and filtering, like `sortText`,
		`filterText`, `insertText`, and `textEdit`, must not be changed during resolve."""
		self.request(method='textDocument/completion', params=params)

	def handle_completion_request(self, context: dict, result: Union[List[CompletionItem], CompletionList, None]) -> None:
		""""""

	def completion_resolve_request(self, params: CompletionItem) -> None:
		"""Request to resolve additional information for a given completion item.The request's
		parameter is of type {@link CompletionItem} the response
		is of type {@link CompletionItem} or a Thenable that resolves to such."""
		self.request(method='completionItem/resolve', params=params)

	def handle_completion_resolve_request(self, context: dict, result: CompletionItem) -> None:
		""""""

	def hover_request(self, params: HoverParams) -> None:
		"""Request to request hover information at a given text document position. The request's
		parameter is of type {@link TextDocumentPosition} the response is of
		type {@link Hover} or a Thenable that resolves to such."""
		self.request(method='textDocument/hover', params=params)

	def handle_hover_request(self, context: dict, result: Union[Hover, None]) -> None:
		""""""

	def signature_help_request(self, params: SignatureHelpParams) -> None:
		self.request(method='textDocument/signatureHelp', params=params)

	def handle_signature_help_request(self, context: dict, result: Union[SignatureHelp, None]) -> None:
		""""""

	def definition_request(self, params: DefinitionParams) -> None:
		"""A request to resolve the definition location of a symbol at a given text
		document position. The request's parameter is of type {@link TextDocumentPosition}
		the response is of either type {@link Definition} or a typed array of
		{@link DefinitionLink} or a Thenable that resolves to such."""
		self.request(method='textDocument/definition', params=params)

	def handle_definition_request(self, context: dict, result: Union[Definition, List[DefinitionLink], None]) -> None:
		""""""

	def references_request(self, params: ReferenceParams) -> None:
		"""A request to resolve project-wide references for the symbol denoted
		by the given text document position. The request's parameter is of
		type {@link ReferenceParams} the response is of type
		{@link Location Location[]} or a Thenable that resolves to such."""
		self.request(method='textDocument/references', params=params)

	def handle_references_request(self, context: dict, result: Union[List[Location], None]) -> None:
		""""""

	def document_highlight_request(self, params: DocumentHighlightParams) -> None:
		"""Request to resolve a {@link DocumentHighlight} for a given
		text document position. The request's parameter is of type {@link TextDocumentPosition}
		the request response is an array of type {@link DocumentHighlight}
		or a Thenable that resolves to such."""
		self.request(method='textDocument/documentHighlight', params=params)

	def handle_document_highlight_request(self, context: dict, result: Union[List[DocumentHighlight], None]) -> None:
		""""""

	def document_symbol_request(self, params: DocumentSymbolParams) -> None:
		"""A request to list all symbols found in a given text document. The request's
		parameter is of type {@link TextDocumentIdentifier} the
		response is of type {@link SymbolInformation SymbolInformation[]} or a Thenable
		that resolves to such."""
		self.request(method='textDocument/documentSymbol', params=params)

	def handle_document_symbol_request(self, context: dict, result: Union[List[SymbolInformation], List[DocumentSymbol], None]) -> None:
		""""""

	def code_action_request(self, params: CodeActionParams) -> None:
		"""A request to provide commands for the given text document and range."""
		self.request(method='textDocument/codeAction', params=params)

	def handle_code_action_request(self, context: dict, result: Union[List[Union[Command, CodeAction]], None]) -> None:
		""""""

	def code_action_resolve_request(self, params: CodeAction) -> None:
		"""Request to resolve additional information for a given code action.The request's
		parameter is of type {@link CodeAction} the response
		is of type {@link CodeAction} or a Thenable that resolves to such."""
		self.request(method='codeAction/resolve', params=params)

	def handle_code_action_resolve_request(self, context: dict, result: CodeAction) -> None:
		""""""

	def workspace_symbol_request(self, params: WorkspaceSymbolParams) -> None:
		"""A request to list project-wide symbols matching the query string given
		by the {@link WorkspaceSymbolParams}. The response is
		of type {@link SymbolInformation SymbolInformation[]} or a Thenable that
		resolves to such.

		@since 3.17.0 - support for WorkspaceSymbol in the returned data. Clients
		 need to advertise support for WorkspaceSymbols via the client capability
		 `workspace.symbol.resolveSupport`.
		"""
		self.request(method='workspace/symbol', params=params)

	def handle_workspace_symbol_request(self, context: dict, result: Union[List[SymbolInformation], List[WorkspaceSymbol], None]) -> None:
		""""""

	def workspace_symbol_resolve_request(self, params: WorkspaceSymbol) -> None:
		"""A request to resolve the range inside the workspace
		symbol's location.

		@since 3.17.0"""
		self.request(method='workspaceSymbol/resolve', params=params)

	def handle_workspace_symbol_resolve_request(self, context: dict, result: WorkspaceSymbol) -> None:
		""""""

	def code_lens_request(self, params: CodeLensParams) -> None:
		"""A request to provide code lens for the given text document."""
		self.request(method='textDocument/codeLens', params=params)

	def handle_code_lens_request(self, context: dict, result: Union[List[CodeLens], None]) -> None:
		""""""

	def code_lens_resolve_request(self, params: CodeLens) -> None:
		"""A request to resolve a command for a given code lens."""
		self.request(method='codeLens/resolve', params=params)

	def handle_code_lens_resolve_request(self, context: dict, result: CodeLens) -> None:
		""""""

	def handle_code_lens_refresh_request(self, context: dict, params: None) -> None:
		""""""

	def document_link_request(self, params: DocumentLinkParams) -> None:
		"""A request to provide document links"""
		self.request(method='textDocument/documentLink', params=params)

	def handle_document_link_request(self, context: dict, result: Union[List[DocumentLink], None]) -> None:
		""""""

	def document_link_resolve_request(self, params: DocumentLink) -> None:
		"""Request to resolve additional information for a given document link. The request's
		parameter is of type {@link DocumentLink} the response
		is of type {@link DocumentLink} or a Thenable that resolves to such."""
		self.request(method='documentLink/resolve', params=params)

	def handle_document_link_resolve_request(self, context: dict, result: DocumentLink) -> None:
		""""""

	def document_formatting_request(self, params: DocumentFormattingParams) -> None:
		"""A request to format a whole document."""
		self.request(method='textDocument/formatting', params=params)

	def handle_document_formatting_request(self, context: dict, result: Union[List[TextEdit], None]) -> None:
		""""""

	def document_range_formatting_request(self, params: DocumentRangeFormattingParams) -> None:
		"""A request to format a range in a document."""
		self.request(method='textDocument/rangeFormatting', params=params)

	def handle_document_range_formatting_request(self, context: dict, result: Union[List[TextEdit], None]) -> None:
		""""""

	def document_ranges_formatting_request(self, params: DocumentRangesFormattingParams) -> None:
		"""A request to format ranges in a document.

		@since 3.18.0
		@proposed"""
		self.request(method='textDocument/rangesFormatting', params=params)

	def handle_document_ranges_formatting_request(self, context: dict, result: Union[List[TextEdit], None]) -> None:
		""""""

	def document_on_type_formatting_request(self, params: DocumentOnTypeFormattingParams) -> None:
		"""A request to format a document on type."""
		self.request(method='textDocument/onTypeFormatting', params=params)

	def handle_document_on_type_formatting_request(self, context: dict, result: Union[List[TextEdit], None]) -> None:
		""""""

	def rename_request(self, params: RenameParams) -> None:
		"""A request to rename a symbol."""
		self.request(method='textDocument/rename', params=params)

	def handle_rename_request(self, context: dict, result: Union[WorkspaceEdit, None]) -> None:
		""""""

	def prepare_rename_request(self, params: PrepareRenameParams) -> None:
		"""A request to test and perform the setup necessary for a rename.

		@since 3.16 - support for default behavior"""
		self.request(method='textDocument/prepareRename', params=params)

	def handle_prepare_rename_request(self, context: dict, result: Union[PrepareRenameResult, None]) -> None:
		""""""

	def execute_command_request(self, params: ExecuteCommandParams) -> None:
		"""A request send from the client to the server to execute a command. The request might return
		a workspace edit which the client will apply to the workspace."""
		self.request(method='workspace/executeCommand', params=params)

	def handle_execute_command_request(self, context: dict, result: Union[LSPAny, None]) -> None:
		""""""

	def handle_apply_workspace_edit_request(self, context: dict, params: ApplyWorkspaceEditParams) -> ApplyWorkspaceEditResult:
		""""""

	def did_change_workspace_folders_notification(self, params: DidChangeWorkspaceFoldersParams) -> None:
		"""The `workspace/didChangeWorkspaceFolders` notification is sent from the client to the server when the workspace
		folder configuration changes."""
		self.notify(method='workspace/didChangeWorkspaceFolders', params=params)

	def work_done_progress_cancel_notification(self, params: WorkDoneProgressCancelParams) -> None:
		"""The `window/workDoneProgress/cancel` notification is sent from  the client to the server to cancel a progress
		initiated on the server side."""
		self.notify(method='window/workDoneProgress/cancel', params=params)

	def did_create_files_notification(self, params: CreateFilesParams) -> None:
		"""The did create files notification is sent from the client to the server when
		files were created from within the client.

		@since 3.16.0"""
		self.notify(method='workspace/didCreateFiles', params=params)

	def did_rename_files_notification(self, params: RenameFilesParams) -> None:
		"""The did rename files notification is sent from the client to the server when
		files were renamed from within the client.

		@since 3.16.0"""
		self.notify(method='workspace/didRenameFiles', params=params)

	def did_delete_files_notification(self, params: DeleteFilesParams) -> None:
		"""The will delete files request is sent from the client to the server before files are actually
		deleted as long as the deletion is triggered from within the client.

		@since 3.16.0"""
		self.notify(method='workspace/didDeleteFiles', params=params)

	def did_open_notebook_document_notification(self, params: DidOpenNotebookDocumentParams) -> None:
		"""A notification sent when a notebook opens.

		@since 3.17.0"""
		self.notify(method='notebookDocument/didOpen', params=params)

	def did_change_notebook_document_notification(self, params: DidChangeNotebookDocumentParams) -> None:
		self.notify(method='notebookDocument/didChange', params=params)

	def did_save_notebook_document_notification(self, params: DidSaveNotebookDocumentParams) -> None:
		"""A notification sent when a notebook document is saved.

		@since 3.17.0"""
		self.notify(method='notebookDocument/didSave', params=params)

	def did_close_notebook_document_notification(self, params: DidCloseNotebookDocumentParams) -> None:
		"""A notification sent when a notebook closes.

		@since 3.17.0"""
		self.notify(method='notebookDocument/didClose', params=params)

	def initialized_notification(self, params: InitializedParams) -> None:
		"""The initialized notification is sent from the client to the
		server after the client is fully initialized and the server
		is allowed to send requests from the server to the client."""
		self.notify(method='initialized', params=params)

	def exit_notification(self, params: None) -> None:
		"""The exit event is sent from the client to the server to
		ask the server to exit its process."""
		self.notify(method='exit', params=params)

	def did_change_configuration_notification(self, params: DidChangeConfigurationParams) -> None:
		"""The configuration change notification is sent from the client to the server
		when the client's configuration has changed. The notification contains
		the changed configuration as defined by the language client."""
		self.notify(method='workspace/didChangeConfiguration', params=params)

	def handle_show_message_notification(self, context: dict, params: ShowMessageParams) -> None:
		""""""

	def handle_log_message_notification(self, context: dict, params: LogMessageParams) -> None:
		""""""

	def handle_telemetry_event_notification(self, context: dict, params: LSPAny) -> None:
		""""""

	def did_open_text_document_notification(self, params: DidOpenTextDocumentParams) -> None:
		"""The document open notification is sent from the client to the server to signal
		newly opened text documents. The document's truth is now managed by the client
		and the server must not try to read the document's truth using the document's
		uri. Open in this sense means it is managed by the client. It doesn't necessarily
		mean that its content is presented in an editor. An open notification must not
		be sent more than once without a corresponding close notification send before.
		This means open and close notification must be balanced and the max open count
		is one."""
		self.notify(method='textDocument/didOpen', params=params)

	def did_change_text_document_notification(self, params: DidChangeTextDocumentParams) -> None:
		"""The document change notification is sent from the client to the server to signal
		changes to a text document."""
		self.notify(method='textDocument/didChange', params=params)

	def did_close_text_document_notification(self, params: DidCloseTextDocumentParams) -> None:
		"""The document close notification is sent from the client to the server when
		the document got closed in the client. The document's truth now exists where
		the document's uri points to (e.g. if the document's uri is a file uri the
		truth now exists on disk). As with the open notification the close notification
		is about managing the document's content. Receiving a close notification
		doesn't mean that the document was open in an editor before. A close
		notification requires a previous open notification to be sent."""
		self.notify(method='textDocument/didClose', params=params)

	def did_save_text_document_notification(self, params: DidSaveTextDocumentParams) -> None:
		"""The document save notification is sent from the client to the server when
		the document got saved in the client."""
		self.notify(method='textDocument/didSave', params=params)

	def will_save_text_document_notification(self, params: WillSaveTextDocumentParams) -> None:
		"""A document will save notification is sent from the client to the server before
		the document is actually saved."""
		self.notify(method='textDocument/willSave', params=params)

	def did_change_watched_files_notification(self, params: DidChangeWatchedFilesParams) -> None:
		"""The watched files notification is sent from the client to the server when
		the client detects changes to file watched by the language client."""
		self.notify(method='workspace/didChangeWatchedFiles', params=params)

	def handle_publish_diagnostics_notification(self, context: dict, params: PublishDiagnosticsParams) -> None:
		""""""

	def set_trace_notification(self, params: SetTraceParams) -> None:
		self.notify(method='$/setTrace', params=params)

	def handle_log_trace_notification(self, context: dict, params: LogTraceParams) -> None:
		""""""

	def cancel_notification(self, params: CancelParams) -> None:
		self.notify(method='$/cancelRequest', params=params)

	def handle_cancel_notification(self, context: dict, params: CancelParams) -> None:
		""""""

	def progress_notification(self, params: ProgressParams) -> None:
		self.notify(method='$/progress', params=params)

	def handle_progress_notification(self, context: dict, params: ProgressParams) -> None:
		""""""

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
			'window/showMessage': self.handle_show_message_notification,
			'window/logMessage': self.handle_log_message_notification,
			'telemetry/event': self.handle_telemetry_event_notification,
			'textDocument/publishDiagnostics': self.handle_publish_diagnostics_notification,
			'$/logTrace': self.handle_log_trace_notification,
			'$/cancelRequest': self.handle_cancel_notification,
			'$/progress': self.handle_progress_notification
			}
		return handle_map[method](params_or_result)

