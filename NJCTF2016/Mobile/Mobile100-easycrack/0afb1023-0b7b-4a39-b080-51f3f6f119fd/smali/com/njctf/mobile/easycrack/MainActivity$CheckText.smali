.class Lcom/njctf/mobile/easycrack/MainActivity$CheckText;
.super Ljava/lang/Object;
.source "MainActivity.java"

# interfaces
.implements Landroid/text/TextWatcher;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/njctf/mobile/easycrack/MainActivity;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = "CheckText"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/njctf/mobile/easycrack/MainActivity;


# direct methods
.method constructor <init>(Lcom/njctf/mobile/easycrack/MainActivity;)V
    .locals 0
    .param p1, "this$0"    # Lcom/njctf/mobile/easycrack/MainActivity;

    .prologue
    .line 30
    iput-object p1, p0, Lcom/njctf/mobile/easycrack/MainActivity$CheckText;->this$0:Lcom/njctf/mobile/easycrack/MainActivity;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public afterTextChanged(Landroid/text/Editable;)V
    .locals 4
    .param p1, "s"    # Landroid/text/Editable;

    .prologue
    .line 32
    iget-object v1, p0, Lcom/njctf/mobile/easycrack/MainActivity$CheckText;->this$0:Lcom/njctf/mobile/easycrack/MainActivity;

    const v2, 0x7f0b0058

    invoke-virtual {v1, v2}, Lcom/njctf/mobile/easycrack/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    .line 33
    .local v0, "tv":Landroid/widget/TextView;
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "Status: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    iget-object v2, p0, Lcom/njctf/mobile/easycrack/MainActivity$CheckText;->this$0:Lcom/njctf/mobile/easycrack/MainActivity;

    invoke-virtual {p1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Lcom/njctf/mobile/easycrack/MainActivity;->parseText(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 34
    return-void
.end method

.method public beforeTextChanged(Ljava/lang/CharSequence;III)V
    .locals 0
    .param p1, "s"    # Ljava/lang/CharSequence;
    .param p2, "start"    # I
    .param p3, "count"    # I
    .param p4, "after"    # I

    .prologue
    .line 38
    return-void
.end method

.method public onTextChanged(Ljava/lang/CharSequence;III)V
    .locals 0
    .param p1, "s"    # Ljava/lang/CharSequence;
    .param p2, "start"    # I
    .param p3, "before"    # I
    .param p4, "count"    # I

    .prologue
    .line 41
    return-void
.end method
